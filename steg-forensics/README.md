# Steganography and Forensics
This document contains challenges meant to go along with the video presentation on steg and forensics.

## Setup
To start up a docker container and a shell:
```
cd steg-forensics 
make
```

## Steg
Move into the steg directory (cd steg).
1. Find the flag in "using-strings"
2. Run strings and binwalk on "using-binwalk" - what information does this tell us?
3. Find the flag in "using-binwalk" (use man binwalk)
4. Find the flag in "using-steghide1" (use man steghide)
5. Using these concepts, find the flag in "using-steghide2"

## Forensics
Move into the forensics directory (cd forensics).
1. Open "traffic1.pcap" in Wireshark (Download [Wireshark](https://www.wireshark.org/download.html))
2. Try filtering HTTP packets and extracting HTTP packets to find the flag
