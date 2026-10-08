# Pinned to python 3.7 to match the original Flask 1.0.2 era behavior
FROM python:3.7-slim

COPY ./source/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./source /app
COPY flag.txt /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
