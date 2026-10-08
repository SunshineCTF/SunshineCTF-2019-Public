# pull official base image
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# build + pillow + psycopg2 dependencies
RUN apk add --no-cache build-base jpeg-dev zlib-dev musl-dev postgresql-dev libffi-dev

# set work directory
WORKDIR /usr/src/exif

# copy reqs
COPY requirements.txt /usr/src/exif

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r /usr/src/exif/requirements.txt

# copy project (exif app -> workdir, victim bot -> /usr/src/victim; replaces the
# old bind mounts so the stack runs without host path mapping)
COPY exif/ /usr/src/exif/
COPY victim/ /usr/src/victim/

ENTRYPOINT ["/usr/src/exif/entrypoint.sh"]
