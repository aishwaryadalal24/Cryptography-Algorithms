import array as arr
import pickle

o=input("enter choice\n1]encrypt\n2]decrypt\n")

if(o=='1'):
    plain_text= input("Enter text to be encrypted: ") 

    k=int(input("enter your key to encrypt data: "))

    k=k%26

    A=arr.array('i')
    s=1
    for i in plain_text:
        if(65<=ord(i) and 90>=ord(i)):
            A.append(ord(i)-64)
        elif(97<=ord(i) and 122>=ord(i)):
            A.append(ord(i)-96)
        s=s+1

    cipher=[]


    for i in A:
        j=(i+k)%26
        if(j==0):
            j=26
        j=j+96
        cipher.append(chr(j))
        
    print(''.join(cipher))
    
    print("Encrypted Successfully!!")

    f1=input("enter file name where you want to store encrypted msg: ")
    f1=f1+".pickle"
    pickle_out=open(f1,"wb")
    pickle.dump(cipher,pickle_out)

    k1=input("enetr file name where you want to store key for decryption : ")
    k1=k1+".pickle"
    pickle_r=open(k1,"wb")
    pickle.dump(k,pickle_r)

    pickle_out.close()

else:
    l=input("enter name of file to be decrypted: ")
    pickle_in=open(l,"rb")
    r=pickle.load(pickle_in)
    l2=input("enter key file name: ")
    pickle_key=open(l2,"rb")
    u=pickle.load(pickle_key)
    h=[]
    B=arr.array('i')
    for i in r:
        if(65<=ord(i) and 90>=ord(i)):
            B.append(ord(i)-64)
        elif(97<=ord(i) and 122>=ord(i)):
            B.append(ord(i)-96)

    for i in B:
        j=(i-u)%26
        if(j==0):
            j=1
        j=j+96
        h.append(chr(j))

    print(''.join(h))


    
