#!/usr/bin/env python2
from PIL import Image, ImageDraw
import requests
import re


#URL = "http://localhost:19505/exam"
URL = "http://archive.sunshinectf.org:19005/exam"

# Need requests session because you need cookies to keep track of your progress
s = requests.Session()

# get first exam
r = s.get(URL)
# Complete 10 exams
for j in range(10):
    # Pull all html list components into stuff list
    # this will include the problems and their multiple choice options
    solutions = []
    stuff = re.findall(r'<li>(.+?)</li>', r.text)

    # if you divide the stuff list into lists of 5
    # you get lists that contain the a problem and 5 answer options
    # for each problem
    for n in range(20):
        # extract and solve problem
        problem = stuff[n*5:n*5+5]
        ans = str(eval(problem[0].replace("/","//")))
        # if the solution isn't in the multiple choice options then cry
        if ans not in problem:
            print "error"
            exit()
        # keep track of the solutions to each problem
        # 0-3 = A-D
        solutions.append(problem.index(ans)-1)

    # Open up the original scantron image with Pillow
    im = Image.open('source/static/scantron.png')
    draw = ImageDraw.Draw(im)

    # x and y for question ! bubble A
    startx = 360
    starty = 460
    # difference between two questions
    height_diff = 90
    # difference between two bubbles
    width_diff = 70
    # radius of the bubble
    r = 30

    # for each problem
    for n in range(20):
        # after problem 9, move over to right column
        if n == 10:
            startx += 490
        # move down to the right problem
        y = starty + (n%10)*(height_diff)
        # fill in the bubble that corresponds to the solution for this problem
        for i in range(5):
            x = startx + (i*width_diff)
            if solutions[n] == i:
                draw.ellipse((x-r, y-r, x+r, y+r), fill = 'black', outline ='black')
    #im.show()
    # save and submit filled out scantron
    im.save("scantron_filled.png")
    files = {'file': open('scantron_filled.png','rb')}
    r = s.post(URL, files=files)
    if "sun" in r.text:
        print r.text
        exit()
