# Wrestler Name Generator
Author: David Maria
## Description
A Server Side Template Injection Challenge. This site is supposed to be a developers project portfolio. The page contains two projects, a "custom greeting" page and a "dynamic page rendering page". The custom greeting page takes a name as input from the URL and displays it on the page with a greeting, and teh dynamic page rendering page allows you to choose which page you want to see renders it for you. On the backend, the dynamic page rendering page will request the template specified in the POST request and render it using a templating engine.
## Solution
Tell the dynamic page rendering page to render the greeting page, and include a template injection payload in the URL of the greeting page, which will be included on the source of the page that will then be rendered by the templating engine. The goal is to read the config, which stores the FLAG in a variable (if you read the unrendered template for admin.html you can see a reference to config.FLAG).

`curl http://folio.sunshinectf.org/render --data "template=hello/{{config}}"`
## Deploy
Run the deploy script
 ```./deploy.sh```
 ## Maintenance
- Just restart or re-provision the Docker container.
