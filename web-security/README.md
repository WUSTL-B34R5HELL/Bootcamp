# Web Security
This document contains challenges meant to go along with the PowerPoint presentation on Web Security <br />
Credit to the [b01lers CTF team](https://b01lers.com/) as this content was inspired by their previous [bootcamp](https://github.com/b01lers/bootcamp-2020-web).

## Setup
```
git clone https://github.com/WUSTL-B34R5HELL/Bootcamp.git
cd Bootcamp/web-security
make
```
## Web Basics
### Example website: localhost:8000
1. Change the website body
2. Change the color of some text
3. Run secretFunc() and place a breakpoint to stop the alert
4. Find any cookies and edit the values
5. Create a new cookie

### Web Challenge: localhost:8001
1. Find the 6 flags, format: bearshell-flag-#{}

## HTTP Server: localhost:8002
1. Send a GET Request to "/flag1"
2. Send a POST Request to "/flag2"
3. Send a GET Request to "/flag3" with two query parameters: 
	password=12345
	extra=bearshell
4. Using BurpSuite or curl, send a POST Request to "/flag4" with a json content-type and 
	password="json-data"

## End
```
make kill
```
