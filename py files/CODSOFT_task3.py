#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

def password_length():
    while True:
        passLength = int(input("Enter length of the password: "))
        if passLength >= 6:
            return passLength
        
        elif passLength <=  0:
            print("Please enter a positive integer.")
        
        elif passLength < 6:
            print("Please enter a integer greater than 6 for strong password.")
        

def generatePassword(length):
    chara = string.ascii_letters + string.digits + string.punctuation
    passw= ''.join(random.choice(chara) for _ in range(length))
    return passw

def main():
    passlen = password_length()
    passw = generatePassword(passlen)
    print("Generated password : ", passw)

main()


# In[ ]:




