FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat python python-dev python-pip && rm -rf /var/lib/apt/lists/*
RUN pip install pycryptodome

WORKDIR /app

COPY server.py .
COPY flag.txt .

CMD socat -T 5 tcp4-l:19003,reuseaddr,fork EXEC:"./server.py",pty,ctty,echo=0
