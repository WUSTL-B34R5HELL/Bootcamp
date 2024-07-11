# Pwn
This document contains challenges meant to go along with the video presentation on binary exploitation

Note: This focuses on the amd64 architecture but can still be run on ARM processors, including the M-series Apple chips.

## Setup
```
cd pwn
make
```

## Buffer Overflow
1. Using gdb, analyze the stack structure of the challenge program
2. Use the buffer overflow vulnerability to call the win() function.
