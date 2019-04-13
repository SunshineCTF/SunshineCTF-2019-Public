#!/bin/bash

docker build -t 16-bit-aes .
docker rm -f 16-bit-aes >/dev/null 2>&1 || true
docker run --name 16-bit-aes -itd --restart=unless-stopped -p 19003:19003 16-bit-aes
