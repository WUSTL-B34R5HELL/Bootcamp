import pwn


#run program
proc = pwn.process("./test_program");

#interact to get flag
i = 1
while i <= 10000:
    proc.sendline(str(i).encode('latin'))
    i += 1

proc.readuntil(b'flag: ')
print(proc.readline().decode('utf-8'))
