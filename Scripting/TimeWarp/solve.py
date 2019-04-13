#!/usr/bin/env python

# James Simmons
# 3/21/2019
# "Time Warp" CTF challenge solution script for SunshineCTF 2019

from pwn import *
import sys

DEBUG = 0
context.log_level = "debug" if DEBUG else "warn"

nums = process("./numbergen")

# r = process("./timewarp")
# r = remote("2019.challenges.sunshinectf.org", 4101)
r = remote("archive.sunshinectf.org", 19004)
# r = remote("localhost", 19004)

while True:
	sys.stdout.write(".")
	num = nums.recvline().strip()
	r.sendline(num)
	correct = r.recvuntil("%s\n" % num)
	debug("correct = %r" % correct)
	response = r.recvline()
	debug("response = %r" % response)
	if "You did it!" in response:
		print("")
		print(r.recvuntil("}"))
		break
