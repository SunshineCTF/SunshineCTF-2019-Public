# WrestlerBook
Author: David Maria

## Description
A sqli challenge where you have to automate using sqli to log in as all users in the DB to find which user has the flag.

## Solution
Use SQL injection to log in as various users until your script sees the flag on the page.

sql injection (into username field)

```' or id==n``` where n is an incrementing integer. This logs you in as different users from the db as you increment n.

## Deploy
Use the primary web deployment script

## Maintenance / Possible issues
- Users do have to brute force, so we may need to run multiple instances if the site gets slow.
- For any other issues, just restart or re-provision the Docker container.
