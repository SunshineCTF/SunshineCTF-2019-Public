FROM python

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./source/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./source /app
COPY flag.txt /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
