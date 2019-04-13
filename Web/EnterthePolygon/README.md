# exifChall
CTF Challenge for BSIDESCTF 19

The application is a user based photo uploading application which proccesses the file as defined in views.py and renders the image and relevant details (exif data). The user has access to their own photo gallery and none other. Relies on Nginx for serving protected images based on user permission through the X-Accel-Redirect header.

**Attackers will need a controlled site to obtain information from their xss payload**

## Worker (Victim)
The worker will run on image save, the signal on the images model will send the filename and user id to the victim rabbitmq queue and the spawn process for the bot will listen to the queue and utilize selenium and phantomjs to navigate to the page. Bot proccess is currently spawned from django settings.py with subprocess.

## Admin Auth
An admin page will exist that relies on the utilization of a static JWT token. The token relies on signing from a resource available from the webserver, easiest resource is w3.css. The attacker then assigns their role to admin and goes to the admin page to get the flag.


## Issues

Most browsers correctly regonize MIME type and will not execute payload, testing requires older browsers.

charset="ISO-8859-1" required if the .jpg extension is not on the loaded script.


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

If you can't get the payload to execute on your end for testing consider if your browser supports the vulnerability. If it does and still having issues with the bot it could be due to your payload, some resources might be blocked or not rendered.

For part 2, common issues: what resource they are signing from, encoding issues (the key is base64 of the given url's content), did they change the user/role?

## Solution

exif image polyglot steals cookie ->


Notes:

register -> login
User forced to input js into image polyglot
execute polygot:
bot visits their page
cookie gets stolen

part 2 -

user will retrieve jwt from part one.
jwt will have username and role - will be static cuz too much effort to make them dynamic
sign against a file contents on the server that the bot has access to.
user changes role to admin -> signs
gets flag on static admin page
