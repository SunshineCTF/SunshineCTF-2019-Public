#!/usr/bin/env python

from Crypto.Cipher import AES
import random
import string

flag = open('flag.txt', 'r').read()

key = random.choice(string.ascii_letters + string.digits) + random.choice(string.ascii_letters + string.digits)

encryptor = AES.new(key*8, AES.MODE_ECB)

def pad(data):
  return data + (16-len(data))*'x'

print 'Welcome, I\'m using an AES-128 cipher with a 16-bit key in ECB mode.\n\nI\'ll give you some help: give me some text, and I\'ll tell you what it looks like\n'
print 'Your text: '
data = raw_input('Your text: ')
print encryptor.encrypt(pad(data)).encode('hex')

random_text = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
print '\nOk, now encrypt this text with the same key: ' + random_text
encrypted_guess = raw_input('Encrypted: ')
try:
  if encrypted_guess == encryptor.encrypt(pad(random_text)) or encrypted_guess.decode('hex') == encryptor.encrypt(pad(random_text)):
    print '\nCorrect! The flag is ' + flag
  else:
    print 'Wrong!'
except:
  print 'Wrong!'
  
