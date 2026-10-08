FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends socat && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pycryptodome

WORKDIR /app

COPY server.py .
COPY flag.txt .
RUN chmod +x server.py

CMD socat -T 60 tcp4-l:19401,reuseaddr,fork EXEC:"./server.py",pty,ctty,echo=0
