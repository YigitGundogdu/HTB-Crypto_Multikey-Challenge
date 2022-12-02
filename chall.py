import os

flag = open("flag.txt", "rb").read()

def genkeys(n):
    keys = [os.urandom(5) for _ in range(n)]
    return keys

def encrypt(keys, flag):
    for key in keys:
        flag = bytes([a ^ b for a, b in zip(flag, key * (len(flag)+5//5))])
    return flag

keys = genkeys(1955) # with this many keys, this is totally secure
print(encrypt(keys, flag).hex())
