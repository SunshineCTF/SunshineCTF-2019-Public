FROM python

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY source/requirements.txt .

RUN pip install -r requirements.txt

COPY source .
COPY flag.txt .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
