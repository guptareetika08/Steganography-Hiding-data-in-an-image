#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import string
import os
d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
x=cv2.imread(r"flower.jpg")
i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter the key to edit(security key)")
text=input("Enter the text to hide in an image")
k1=0
tln=len(text)
z=0
n=0
m=0
l=len(text)
for i in range(1):
    x[n,m,z]=d[text[i]]^d[key[k1]]
    n=n+1
    m=m+1
    m=(m+1)%3
    k1=(k1+1)%len(key)

cv2.imwrite("encrypted_img.jpg",x)
os.startfile("encrypted_img.jpg")
print("Data hiding in image completed successfully!")

k1=0
tln=len(text)
z=0
n=0
m=0
ch=int(input("enter 1 to extract data from image:"))
if ch==1:
    key1=input("re-enter key to extract  text from image")
    decrypt=""
    if key==key1:
        for i in range(1):
            decrypt+=c[x[n,m,z]^d[key[k1]]]
            n=n+1
            m=m+1
            k1=(k1+1)%len(key)
        print("encrypted text:",decrypt)
    else:
        print("key doesn't match")
else:
    print("Thank you, EXITING!")  
                      

