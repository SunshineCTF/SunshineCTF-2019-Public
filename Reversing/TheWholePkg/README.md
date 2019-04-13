#  The Whole Pkg

Author: David Maria

# Description
This challenge consists of a nodeJS application that has been compiled using [pkg](https://github.com/zeit/pkg). Pkg compiled the node source to V8 bytecode, so it won't be possible to retrieve the source from the binary (easily). Pkg also packages all of the assets / files needed by the application into the binary in a virtual file system.

The app is a "strategy vault" that allows you to read a bunch of encrypted files that contain wrestling strategies. Each file is encrypted using AES256 using the same key, and they are packaged inside the binary so users will not be able to see the files, only interact with them through the app. The app allows users to read all of the files, except for the flag.txt file (in the code it checks to see if you're trying to read file #3 and if you are then it says permission denied).

# Solution
See ./solve

Reverse engineer the pkg app to figure out how the snapshot virtual filesystem works, and then move the entities in the snapshot filesystem json object so that when you try to read one of the permitted files, it will  instead read flag.txt.

In the binary:

- Replace the flag entity with the costume_stores file entity, this is necessary so that the length of the file / offsets in the file aren't changed during the next step

- Replace the  costume_stores entity with the flag entity, this will let you read the flag file when you try to read costume_stores.txt


run the application and read sourcing_weapons.txt

# Deploy
Just have the Strategy_Vault-win.exe file available for download.

# Building
- Install nodeJS (This was built using v8.11.1)
- Install npm
- Install pkg golabally
`npm install -g pkg`
- Go into the source folder and run:
`npm install`
- Run:
`pkg .`
