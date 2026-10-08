# exifChall
CTF Challenge for BSIDESCTF 19 (run as "Enter the Polygon" parts 1 and 2 in SunshineCTF 2019)

The application is a user based photo uploading application which proccesses the file as defined in views.py and renders the image and relevant details (exif data). The user has access to their own photo gallery and none other.

------
Static Contents hosted on /nginx/static/*
Media contents hosted on shared volume.


OS Reqs
```
Docker
Docker-compose
```

Python Requirements
```
Pillow
Django==2.1.4
ExifRead==2.1.2
python-jose==3.0.1
gunicorn= "==19.9.0"
psycopg2
pika
selenium
```

## Setup
Modify the compose file's env variable to your need, if you change creds for prebuilt user it will need to be propogated to bot.

Be sure to modify settings.py to update allowed_hosts from wildcard if possible.

Modify APPROVED_SIGNER to external ip/hostname of the nginx instance.



## RUN

docker-compose build

docker-compose up

## Reset state
docker-compose down -v

## Troubleshoot

If the web application/rabbitmq/database is not responding it is best to bring the whole thing down and back up as certain aspects rely to heavily on each other.

If the bot stops issuing requests it can be restarted by killing the bot.py proccess and restarting it at /usr/src/victim/bot.py on the web container; otherwise a full reset will bring the bot back up.

Still having issues? Have you tried resetting it?

See [writeup.md](writeup.md) for the solution to both parts (and further troubleshooting notes that would spoil the solve).
