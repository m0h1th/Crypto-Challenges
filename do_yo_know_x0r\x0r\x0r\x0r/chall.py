import os
from Crypto.Util.Padding import pad
from pwn import xor


key = os.urandom(27)
flag = b"cyberchaze{####################REDACTED####################}"
padenc = pad(flag,?)
enc = xor(padenc,key)
print(enc)
