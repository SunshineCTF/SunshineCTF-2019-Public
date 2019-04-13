#!/bin/bash

docker build -t portfolio .
docker rm -f portfolio >/dev/null 2>&1 || true
docker run --name portfolio -itd --restart=unless-stopped -v /etc/localtime:/etc/localtime:ro --read-only -v /var/run -p 0.0.0.0:5000:5000 portfolio 
