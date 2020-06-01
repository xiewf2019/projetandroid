import json 
import subprocess
import sys
import re
import os


def lec():
    li=[]
    for i in range(95):
        if i==19 or i==37:
            n=0
        else:
            if i<9:
                p="0"+str(i+1)
            else:
                p=str(i+1)
            file ="graphe_depts/"+str(i+1)+".out"
            file1="5pour100/sortie"+p+".txt"
            file2="20pour100/sortie"+p+".txt"
            f=open(file, "r")
            dec = f.readlines()
            f.close()
            l=[int(s) for s in dec[0].split() if s.isdigit()]
            if os.path.isfile(file1):
                f1=open(file1, "r")
                dec1 = f1.readlines()
                f1.close()
                if (len(dec1)<3):
                    if os.path.isfile(file2):
                        f2=open(file2, "r")
                        dec2 = f2.readlines()
                        f2.close()
                        if (len(dec2)<3):
                            n=0
                        else:
                            l2=[int(s) for s in dec2[2].split() if s.isdigit()]
                            n=l2[l[0]]
                    else:
                        n=0
                else:
                    l1=[int(s) for s in dec1[2].split() if s.isdigit()]
                    n=l1[l[0]]
            else:
                n=0
        li.append(n)
    return li
def main():
    file="num_dep.txt"
    f=open(file, "r")
    dec = f.readlines()
    l=[int(s) for s in dec[0].split() if s.isdigit()]
    cd=lec()
    n=cd[l[0]-1]
    f.close()
    l=[]
    str1=""
    
    l.append(dec[0][3:])
    l.append(dec[0][:2])
    l.append(str(n))
    return(l)

def lec1():
    li=[]
    file ="nombre_divise.txt"
    f=open(file, "r")
    dec = f.readlines()
    f.close()
    constraint3 = re.findall(r"[\w']+",dec[0])
    constraint3 = [int(i) for i in constraint3]
    return constraint3
def pas_desolution():
    l=lec1()
    tab=[]
    for i in range(95):
        if l[i] == 1:
            tab.append(i+1)
    return tab



print(main())