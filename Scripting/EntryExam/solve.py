#!/usr/bin/env python3
import os
import re
import sys
from PIL import Image, ImageDraw
import requests

# `pwnmake check` sets URL to the site root (e.g. http://localhost:19202); the
# exam endpoint lives at /exam. Accept either form so manual runs still work.
_BASE = os.environ.get("URL", "http://localhost:19202").rstrip("/")
URL = _BASE if _BASE.endswith("/exam") else _BASE + "/exam"
SCANTRON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source", "static", "scantron.png")

# Need a requests session because cookies track exam progress
s = requests.Session()

# get first exam
r = s.get(URL)
# Complete 10 exams
for j in range(10):
    # Pull all <li> items: the problems and their multiple choice options
    solutions = []
    stuff = re.findall(r'<li>(.+?)</li>', r.text)

    # Each problem is one <li> followed by 4 answer-option <li> items
    for n in range(20):
        problem = stuff[n * 5:n * 5 + 5]
        ans = str(eval(problem[0].replace("/", "//")))
        if ans not in problem:
            print("error")
            sys.exit(1)
        # 0-3 = A-D (offset by the question <li> at index 0)
        solutions.append(problem.index(ans) - 1)

    # Open the original scantron and bubble in answers
    im = Image.open(SCANTRON)
    draw = ImageDraw.Draw(im)

    startx = 360
    starty = 460
    height_diff = 90
    width_diff = 70
    rad = 30

    for n in range(20):
        if n == 10:
            startx += 490
        y = starty + (n % 10) * height_diff
        for i in range(5):
            x = startx + (i * width_diff)
            if solutions[n] == i:
                draw.ellipse((x - rad, y - rad, x + rad, y + rad), fill='black', outline='black')

    im.save("/tmp/scantron_filled.png")
    files = {'file': open("/tmp/scantron_filled.png", 'rb')}
    r = s.post(URL, files=files)
    if "sun" in r.text:
        print(r.text)
        sys.exit(0)

print(r.text)
