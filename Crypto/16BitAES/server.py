#!/usr/bin/env python3

import sys
from Crypto.Cipher import AES
import random
import string

flag = open('flag.txt', 'r').read()

key = random.choice(string.ascii_letters + string.digits) + random.choice(string.ascii_letters + string.digits)

encryptor = AES.new((key * 8).encode(), AES.MODE_ECB)


def pad(data):
    return data + (16 - len(data)) * b'x'


def main():
    print("Welcome, I'm using an AES-128 cipher with a 16-bit key in ECB mode.\n")
    print("I'll give you some help: give me some text, and I'll tell you what it looks like\n")
    sys.stdout.write('Your text: ')
    sys.stdout.flush()
    data = sys.stdin.readline().rstrip('\n').encode()
    print(encryptor.encrypt(pad(data)).hex())

    random_text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    print('\nOk, now encrypt this text with the same key: ' + random_text)
    sys.stdout.write('Encrypted: ')
    sys.stdout.flush()
    encrypted_guess = sys.stdin.readline().rstrip('\n')

    target = encryptor.encrypt(pad(random_text.encode()))
    try:
        if encrypted_guess.encode() == target or bytes.fromhex(encrypted_guess) == target:
            print('\nCorrect! The flag is ' + flag)
        else:
            print('Wrong!')
    except Exception:
        print('Wrong!')


if __name__ == '__main__':
    main()
