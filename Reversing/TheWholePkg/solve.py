import re

with open("Strategy_Vault-win.exe", 'rb') as f:
    content = f.read()

# Pull the file entities from the snapshot filesystem for the flag and for a normal file we have permission to encrypt
flag_entity = re.findall(b'flag.txt":(.+?})', content)
# Example snapshot filesystem entry:
# "C:\\snapshot\\source\\files\\flag.txt" : {
#   "1" : [ // file content
#     18174, // start byte in snapshot filesystem
#     96 //file length
#   ],
#   "3" : [ // file stat
#     18270, 
#     68
#   ]
# }, 
costume_entity = re.findall(b'costume_shops.txt":(.+?})', content)

# Swap the entities around.
# By moving the flag entity to the costume entity, you'll be able to read and decrypt the flag by asking the program to read you the costume file
# You have to swap the flag entity to the costume entity as well to avoid the length of the file changing
content = content.replace(flag_entity[0], b"FLAG_PLACEHOLDER_LMAO")
content = content.replace(costume_entity[0], b"COSTUME_PLACEHOLDER_LMAO")
content = content.replace(b"FLAG_PLACEHOLDER_LMAO", costume_entity[0])
content = content.replace(b"COSTUME_PLACEHOLDER_LMAO", flag_entity[0])

with open("Strategy_Vault-win.exe", 'wb') as f:
    f.write(content)

# After this, run the program and read "costume_stores.txt"
