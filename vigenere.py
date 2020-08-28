import pickle

def create_key(plain_text, key):
    pl=len(plain_text)

    kl=len(key)

    d=int(pl/kl)

    r=pl%kl
    
    key1=""

    for i in range(d):
        key1=key1+key


    j=0
        
    for i in range(r):
        key1=key1+key[j]
        j=j+1
        
    return key1



def encrypt_with_vigenere():

    plain_text=input("Enter the text to encrypt: ")

    key=input("Enter key for encryption: ")

    key1=create_key(plain_text,key)

    pl=len(plain_text)

    cipher_text=""

    for i in range(pl):
        v=((ord(plain_text[i])+ord(key1[i])-192)%26)-1
        if(v==-1):
            v=25

        if(v==0):
            v=26

        cipher_text=cipher_text+chr(v+96)

    print("Encrypted text is:")
    print(cipher_text)
    


def decrypt_with_vigenere():

    cipher_text=input("Enter the text to decrypt: ")

    key=input("Enter key for decryption: ")

    key1=create_key(cipher_text,key)

    cl=len(cipher_text)

    plain_text=""

    for i in range(cl):
        v=((ord(cipher_text[i])-ord(key1[i]))+1)%26
        if(v==-1):
            v=25

        if(v==0):
            v=26

        plain_text=plain_text+chr(v+96)

    print("Original text is:")
    print(plain_text)





if __name__ == "__main__": 
    print("Enter Choice : 1] encrypt \n 2] Decrypt\n")

    choice=input()

    if(choice =='1'):
        encrypt_with_vigenere()

    else:
        decrypt_with_vigenere()

