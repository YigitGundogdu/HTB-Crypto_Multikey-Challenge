import os
import string
def decrypt(key, flag):
    flag = bytes([a ^ b for a, b in zip(flag, key * (len(flag)+5//5))])
    return flag
    
flag = open("output.txt", "r").read()
old_flag=bytes.fromhex(flag)

guessable_part_flag=bytes.fromhex(flag)[:5]

possible_Chars=string.ascii_letters+string.digits
key="HTB{"
#key=key.encode()
guess=[]
for i in possible_Chars:
    part_flag=key+i
    guess.append(part_flag.encode())
for i in guess:
    decrypted= bytes([a ^ b for a, b in zip(guessable_part_flag,i)])
    print(decrypt(decrypted,old_flag))

#HTB{d0_w3_r34lly_n33d_th1s_m4ny_c4r_k3y5_f0r_4_s1lly_t1me_m4ch1n3??}
