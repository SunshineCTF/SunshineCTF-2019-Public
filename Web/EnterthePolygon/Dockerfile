# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# pillow dependencies  https://github.com/python-pillow/Pillow/issues/1763
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev musl-dev postgresql-dev

# set work directory
WORKDIR /usr/src/exif

# copy reqs
COPY requirements.txt /usr/src/exif

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r /usr/src/exif/requirements.txt


# copy project
COPY . /usr/src/exif/

ENTRYPOINT ["/usr/src/exif/entrypoint.sh"]
