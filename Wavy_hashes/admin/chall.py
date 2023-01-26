from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
from secret import iv

xor = lambda a,b : bytes(i^j for i,j in zip(a,b))

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ct = b''
    for block in blocks:
        enc_block = cipher.encrypt(xor(block, iv))
        iv = sha256(iv).digest()[:16]
        ct += enc_block
    return ct

pt = open('secretfile', 'rb').read()
ct = encrypt(pad(pt,16), b'PERFECTLENGTHKEY', iv)
with open('file.enc', 'wb') as f:
    f.write(ct)