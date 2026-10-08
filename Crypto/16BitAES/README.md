# 16 Bit AES

An AES (ECB mode) crypto challenge served over TCP. The server gives the player a string and asks them to send it back encrypted with the correct key.

### Notes
  * Hex encoding used to send ciphertext to/from server
  * Listens on port 19003 (can be changed)

### Deployment
```
./deploy.sh
```

### Solve script
```
pip install pycrypto
./solve.py
```

See [writeup.md](writeup.md) for the solution.
