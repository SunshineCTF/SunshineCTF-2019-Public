# Entry Exam
Author: David Maria

## Description
A scripting challenge where the player has to automate solving a set of 20 multiple choice problem math exams. The solutions to each exam have to be submitted by filling out a PNG image of a scantron as if it were a real scantron, and submitting that to the site within 2 seconds of receiving the exam. After finishing 10 exams successfully, the flag is given.

## Solution
- Use a script to make a get request to the server
- Extract the questions and multiple choice options
- Generate a list of the answers
- Use an image processing library to bubble in the right bubbles on the scantron image
- Post the solution
- Repeat

See `solve.py`.

## Deploy
Run the deploy script `./deploy.sh`. This script builds the docker container for the challenge

## Maintenance
- Just restart or re-provision the Docker container.
