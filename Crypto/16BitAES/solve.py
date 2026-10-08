#!/usr/bin/env python3

import os
import sys
import string
from pwn import remote, context
try:
    from Crypto.Cipher import AES
except ImportError:  # some distros ship pycryptodome under the Cryptodome namespace
    from Cryptodome.Cipher import AES

context.log_level = "warn"

# Read target from the environment so `pwnmake check` can drive HOST/PORT
HOST = os.environ.get("HOST") or (sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1")
PORT = int(os.environ.get("PORT") or (sys.argv[2] if len(sys.argv) > 2 else 19401))

characters = string.ascii_letters + string.digits
teststring = b'a' * 16

r = remote(HOST, PORT)
r.recvuntil(b'Your text: ')
r.sendline(teststring)

# The server prints the hex ciphertext of our chosen plaintext
encrypted = r.recvline().strip().decode()

# Brute force the 2-character (16-bit) key offline
found = None
for i in characters:
    for j in characters:
        key = (i + j) * 8
        aes = AES.new(key.encode(), AES.MODE_ECB)
        if aes.encrypt(teststring).hex() == encrypted:
            found = key
            break
    if found:
        break

assert found, "key not found"

# Grab the challenge text and send back the correct ciphertext
r.recvuntil(b'same key: ')
text = r.recvline().strip()
r.recvuntil(b'Encrypted: ')
aes = AES.new(found.encode(), AES.MODE_ECB)
r.sendline(aes.encrypt(text).hex().encode())

print(r.recvall(timeout=5).decode(errors="replace"))
