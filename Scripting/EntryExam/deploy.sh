#!/bin/bash

docker build -t scantron .
docker rm -f scantron >/dev/null 2>&1 || true
docker run --name scantron -itd --restart=unless-stopped -v /etc/localtime:/etc/localtime:ro --read-only -v /var/run -p 127.0.0.1:19505:5000 scantron 
