# Linux and Scripting
This document contains small challenges meant to go along with the PowerPoint presentation on Linux and Shell CLI, and python scripting.

## Linux CLI and Shell
### Navigating the File System
1. Create an empty file named "bearshell"
2. Write "Hello World!" inside the file
3. Create a directory named "beardir" and move into this directory
4. Move the file into the directory
5. Copy the file outside the directory

### Command Flags and Man pages
1. Print out the contents of the "beardir" directory
2. Print out the permissions of the files
3. Print out hidden files

### File Permissions
1. What are the current permissions of the "bearshell" file
2. Change the permissions of the "bearshell" file so that it is executable and suid bit is set
2. Reprint the permssions of the file
3. Change the owner to root (need sudo/root permissions)

### Netcat
1. Listen on port 8888 using netcat
2. Connect to this port using another instance of netcat and send a message from the server and from the client

### Piping and Redirection
1. Without a text editor, write "redirection is cool\n" into the "bearshell" file
2. Print out the contents of this file
3. Repeat step 1 without overriding the file
4. Run ps aux
5. View "ps aux" in less


## Python Scripting
### Automating Program Input
See script.py. This script automates the process of inputing 1 to 10,000 into the test program.