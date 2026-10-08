# Pinned to python 3.7 to match the original Flask 1.0.2 era behavior
FROM python:3.7-slim

WORKDIR /app

COPY source/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY source .
COPY flag.txt .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
