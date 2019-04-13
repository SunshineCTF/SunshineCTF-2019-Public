#!/bin/bash

docker build -t namegen --build-arg "FLAG=$(cat flag.txt)" .
docker rm -f namegen >/dev/null 2>&1 || true
docker run --name namegen -itd --restart=unless-stopped -v /etc/localtime:/etc/localtime:ro --read-only -v /var/run -p 127.0.0.1:19507:80 namegen
