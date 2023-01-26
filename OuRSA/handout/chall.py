from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random
import time
from secret import flag
from gmpy2 import next_prime

def getWeirdPrime():
    p = random.getrandbits(30) ^ 1<<31
    while p.bit_length()<1024:
        p = (p<<32) ^ p
    return int(next_prime(p))

p = getWeirdPrime()
q = getPrime(1024)
n = p*q
e = 65537

ct = pow(flag,e,n)

print(f'{n=}')
print(f'{e=}')
print(f'{ct=}')