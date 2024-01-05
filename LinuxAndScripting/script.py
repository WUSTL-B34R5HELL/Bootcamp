import pwn


#run program
proc = pwn.process("./test_program");

#interact to get flag
out = b""
i = 1
while i <= 10000:
    proc.sendline(str(i).encode('latin'))
    i += 1

proc.readuntil(b'flag:')
print(proc.readline())
