# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:18:21 2021

@author: SIDDHANT
"""
import pickle
import os
def inp(s):
    fin=open(s,'ab+')
    while True:
        ID=input("Enter ID ")
        name=input("Enter name ")
        mydict={}
        mydict[ID]=name
        pickle.dump(mydict,fin)
        y=input("Exit?y/n ")
        if y=='y':
            break
    fin.close()
def edit(s):
    file=open(s,"rb")
    file2=open(s[:-4]+"1.dat","wb")
    ID=input("Enter ID ")
    newName=input("Enter new name")
    flag=False
    try:
        while True:
            l=pickle.load(file)
            if ID in l:
                flag=True
                l[ID]=newName
            pickle.dump(l,file2)
    except Exception as e:
        if flag:
            file.close()
            file2.close()
            os.remove(s)
            os.rename(s[:-4]+"1.dat",s)
            print("Update successful")
        else:
            print(e)
            print("Record not found")
def read(s):
    file=open(s,'rb')
    try:
        while True:
            l=pickle.load(file)
            for i in l:
                print(i," ",l[i])
    except:
        pass
    file.close()
s=r"INPUT YOUR FILE HERE"
#inp(s)
edit(s)
read(s)