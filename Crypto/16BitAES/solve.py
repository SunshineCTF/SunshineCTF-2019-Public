#!/usr/bin/env python

from pwn import *
from Crypto.Cipher import AES
import sys
import time

characters = string.ascii_letters + string.digits

teststring = 'a'*16

r = remote('127.0.0.1', 19003)
print r.recvuntil('Your text:')
r.sendline(teststring)
encrypted = r.recvuntil('key:').split('\n')[1].strip()

print 'Looking for encryption of', teststring, 'that equals', encrypted

key = None
for i in characters:
  for j in characters:
    key = i + j

    aes = AES.new(key*8, AES.MODE_ECB)
    print 'Trying', key, '-', aes.encrypt(teststring).encode('hex')

    if aes.encrypt(teststring).encode('hex').strip() == encrypted:

      text = r.recvline().strip()
      print 'Going to encrypt', text
      r.sendline(aes.encrypt(text).encode('hex'))
      print r.recv()

      sys.exit(0)

