# 16 Bit AES

This is a simple brute force challenge that gives the user a string and asks them to encrypt the string with the correct AES key in ECB mode.

### Given to the user
  * AES in ECB mode
  * An oracle that returns the encrypted text for any plaintext

### Required to solve
  * Use brute force to determine the AES key used to encrypt the chosen plaintext
  * Key insight: Smallest AES is 256, so a 16 bit key would have to be repeated 8 times to form the full 256 bit key
  * Encrypt the message from the server using the determined key and send back to server

### Notes
  * Hex encoding used to send ciphertext to/from server
  * Listens on port 19003 (can be changed)
  * Brute force can be done using requests to server, but is much easier to do offline

### Hints
  * How can an AES-128 key be made with only 16 bits?  There's only a few ways to fill the rest of the 112 bits, so try them.
  * What is the issue with having such a small keyspace? (Brute force is possible)

### Deployment
```
./deploy.sh
```

### Solve script
```
pip install pycrypto
./solve.py
```
