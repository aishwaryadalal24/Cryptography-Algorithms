#rail fence

import numpy as np

def create_rail(pl,d,text):

    if(pl%d==0):
        n=int(pl/d)
    else:
        n=int(pl/d)+1

    key_arr=np.chararray((d,n))
    k=0
    for i in range(n):
        for j in range(d):
            key_arr[j][i]=text[k]
            k=k+1
            if(k==pl):
                break

    return key_arr


def decreate_rail(pl,d,text):
    if(pl%d==0):
        n=int(pl/d)
    else:
        n=int(pl/d)+1

    key_arr=np.chararray((d,n))
    k=0
    for i in range(d):
        for j in range(n):
            key_arr[i][j]=text[k]
            k=k+1
            if(k==pl):
                break
            
    return key_arr
    
    



def encrypt_with_RailFence():

    plain_text=input("Enter text to be encrypted: ")
    depth=int(input("Enter the Depth of rail you want: "))

    plain_text=plain_text.replace(' ', '')

    pl=len(plain_text)

    key_arr=create_rail(pl,depth,plain_text)

    d=depth

    if(pl%d==0):
        n=int(pl/d)
    else:
        n=int(pl/d)+1
    

    cipher_text=[]
    k=0
    for i in range(d):
        for j in range(n):
            cipher_text.append(key_arr[i][j])
            k=k+1
            if(k==pl):
                break

    print("Encrypted text is: "+str(b"".join(cipher_text),'utf-8'))
    



def decrypt_with_RailFence():

    cipher_text=input("Enter text to be encrypted: ")

    depth=int(input("Enter the Depth of rail you want: "))

    cipher_text=cipher_text.replace(' ', '')

    cl=len(cipher_text)

    key_arr=decreate_rail(cl,depth,cipher_text)

    plain_text=[]
    d=depth
    if(cl%d==0):
        n=int(cl/d)
    else:
        n=int(cl/d)+1
    k=0
    for i in range(n):
        for j in range(d):
            plain_text.append(key_arr[j][i])
            k=k+1
            if(k==cl):
                break
            
            
    print("decrypted text is: "+str(b"".join(plain_text),'utf-8'))
    

if __name__ == "__main__": 
    print("Enter Choice : 1] encrypt with RailFence \n 2] Decrypt with RailFence\n")

    choice=input()

    if(choice =='1'):
        encrypt_with_RailFence()

    else:
        decrypt_with_RailFence()

