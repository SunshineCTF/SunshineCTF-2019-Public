Challenge Name: Castles
Author: snak
Given: Castles.001
Description: The flag might be in another castle.
Hint: If you are almost there, someone may have used STEG to HIDE something.

Flag: flag{7H4NK5_F0R_PL4Y1NG} ***Note is not in "sun{flag} format"***

Deployment: Just distribute the file and have players download it.

Solution:
You are given a file (Castles.001). This image is really a bit level copy of a flash drive. By looking at the file system with a tool such as WinHex or Autopsy you will be able find 5 files. 4 are named as the castles they are shown and the fifth is named “AlmostThere.jpg”. Depending on the tool you use you might see that this file has been deleted but not overwritten.
As the hint says, “If you are almost there, someone may have used STEG to HIDE something”. This is a pretty heavy point to the tool steghide. This tool requires a key to extract a message hidden within. Finding that key is a big part of the challenge.

By examining device slack space you will find a message: 
“peachPeachPEACH Hey! Mario said something about a hidden key. Hesaid this: F2I and A1S, and that it was in two pieces.”
This is supposed to help you figure out that the key is split in two. The two halves are between the 1st and 2nd image and between the 3rd and 4th image.
 
There are 4 castles: Feira, Inveraray, Amorosa, and Spis. If you take the first letter of each name the hint refers to the images. The second half of the key is somewhere between Feira and Inveraray and the first half is located between Amorosa and Spis.
The first half of the key is located at offset: 000650992 and is “AQ273RFGHUI91O”.
The second half of the key is located at offset: 000280560 and is “LO987YTFGY78IK”.
The full key then is “AQ273RFGHUI91OLO987YTFGY78IK”.

Now all there is left to do is use steghide with the key above to extract the flag that it is carrying.
The flag is: “flag{7H4NK5_F0R_PL4Y1NG}”
