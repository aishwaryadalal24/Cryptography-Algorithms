import pickle
from collections import OrderedDict 
import array as arr
import numpy as np
import struct
 

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))  


def key_array_generator(key):
    key=removeDupWithOrder(key)
    key=key.replace('j', '')
    
    for i in range(97,123):
        if(chr(i) not in key):
            key=key+chr(i)
            
    key=key.replace('j', '')
    
    key_arr=np.chararray((5,5))
    k=0
    for i in range(5):
        for j in range(5):
            key_arr[i][j]=key[k]
            k=k+1
            
    return key_arr
    

def encrypt_with_playfair():

    plain_text=input("Enter text to be encrypted: ")

    key=input("enter key for encryption: ")
   
    plain_text=plain_text.replace(' ', '')

    
    
    
    key_arr=key_array_generator(key)
        
    
    
    print(key_arr)
    i=0

    while(i<len(plain_text)-1):
        if(plain_text[i]==plain_text[i+1]):
            plain_text=plain_text[:i]+'x'+plain_text[i:]
        i=i+2
    
    if(len(plain_text)%2==1):
        plain_text=plain_text+'x'
      
    cipher_text=[]
    i=0
    while(i<len(plain_text)-1):
        h1=struct.pack('b',ord(plain_text[i]))
        h2=struct.pack('b',ord(plain_text[i+1]))
        r1,c1=np.where(key_arr==h1)
        r2,c2=np.where(key_arr==h2)
        r1=int(r1)
        r2=int(r2)
        c1=int(c1)
        c2=int(c2)
        
        if(r1==r2):
            cipher_text.append(key_arr[(r1+1)%5][c1])
            cipher_text.append(key_arr[(r2+1)%5][c2])
            
        elif(c1==c2):
            cipher_text.append(key_arr[r1][(c1+1)%5])
            cipher_text.append(key_arr[r2][(c2+1)%5])
            
        else:
            cipher_text.append(key_arr[r1][c2])
            cipher_text.append(key_arr[r2][c1])
        i=i+2
            
            
    print("Encrypted message is:")
    print(str(b"".join(cipher_text),'utf-8'))
    
    
    


def decrypt_with_playfair():
    cipher_text=input("enter text to be decrypted: ")
    key=input("enter key for decryption: ")
   
    cipher_text=cipher_text.replace(' ', '')
    
    key_arr=key_array_generator(key)
    
    i=0

      
    plain_text=[]
    i=0
    while(i<len(cipher_text)-1):
        h1=struct.pack('b',ord(cipher_text[i]))
        h2=struct.pack('b',ord(cipher_text[i+1]))
        r1,c1=np.where(key_arr==h1)
        r2,c2=np.where(key_arr==h2)
        r1=int(r1)
        r2=int(r2)
        c1=int(c1)
        c2=int(c2)
        
        if(r1==r2):
            if(r1==0):
                r1=5
                r2=5
            plain_text.append(key_arr[(r1-1)%5][c1])
            plain_text.append(key_arr[(r2-1)%5][c2])
            
        elif(c1==c2):
            if(c1==0):
                c1=5
                c2=5
            plain_text.append(key_arr[r1][(c1-1)%5])
            plain_text.append(key_arr[r2][(c2-1)%5])
            
        else:
            plain_text.append(key_arr[r1][c2])
            plain_text.append(key_arr[r2][c1])
        i=i+2
            
    if(plain_text[len(plain_text)-1]==b'x'):
        plain_text = plain_text[:-1]
    print("decrypted message is:")
    print(str(b"".join(plain_text),'utf-8'))
    
    
    



if __name__ == "__main__": 
    print("Enter Choice : 1] encrypt \n 2] Decrypt\n")

    choice=input()

    if(choice =='1'):
        encrypt_with_playfair()

    else:
        decrypt_with_playfair()
