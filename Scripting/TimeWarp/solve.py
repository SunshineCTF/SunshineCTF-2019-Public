#!/usr/bin/env python3

# James Simmons
# 3/21/2019
# "Time Warp" CTF challenge solution script for SunshineCTF 2019
# (ported to python3 / pwntools 4.x for the archive)

from pwn import *
import sys
import os

DEBUG = 0
context.log_level = "debug" if DEBUG else "warn"

# Read target from the environment so `pwnmake check` can drive HOST/PORT
HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", 19201))

# numbergen replays the same srand(301570435) sequence the challenge uses
nums = process(".build/numbergen" if os.path.exists(".build/numbergen") else "./numbergen")

r = remote(HOST, PORT)

while True:
	sys.stdout.write(".")
	sys.stdout.flush()
	num = nums.recvline().strip()
	r.sendline(num)
	r.recvuntil(num + b"\n")
	response = r.recvline()
	debug("response = %r" % response)
	if b"You did it!" in response:
		print("")
		print(r.recvuntil(b"}").decode(errors="replace"))
		break
