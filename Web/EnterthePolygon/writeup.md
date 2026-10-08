# Enter the Polygon Writeup

The application relies on Nginx for serving protected images based on user permission through the X-Accel-Redirect header.

**Attackers will need a controlled site to obtain information from their xss payload**

## Worker (Victim)
The worker will run on image save, the signal on the images model will send the filename and user id to the victim rabbitmq queue and the spawn process for the bot will listen to the queue and utilize selenium and phantomjs to navigate to the page. Bot proccess is currently spawned from django settings.py with subprocess.

## Part 1

exif image polyglot steals cookie ->

Notes:

register -> login
User forced to input js into image polyglot
execute polygot:
bot visits their page
cookie gets stolen

## Part 2

### Admin Auth
An admin page will exist that relies on the utilization of a static JWT token. The token relies on signing from a resource available from the webserver, easiest resource is w3.css. The attacker then assigns their role to admin and goes to the admin page to get the flag.

### Notes

user will retrieve jwt from part one.
jwt will have username and role - will be static cuz too much effort to make them dynamic
sign against a file contents on the server that the bot has access to.
user changes role to admin -> signs
gets flag on static admin page

## Issues

Most browsers correctly regonize MIME type and will not execute payload, testing requires older browsers.

charset="ISO-8859-1" required if the .jpg extension is not on the loaded script.

## Troubleshooting (spoilers)

If you can't get the payload to execute on your end for testing consider if your browser supports the vulnerability. If it does and still having issues with the bot it could be due to your payload, some resources might be blocked or not rendered.

For part 2, common issues: what resource they are signing from, encoding issues (the key is base64 of the given url's content), did they change the user/role?
