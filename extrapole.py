#!/usr/bin/env python

import json 
import subprocess
import sys
import re


def lecture(num):
    if(num<10):
        file="sortie0"+str(num)+".txt"
    else:
        file="sortie"+str(num)+".txt"
    file1="5pour100/"+file
    file2="20pour100/"+file
    f = open(file1, "r")
    dec = f.readlines()
    f.close()
    if (len(dec)<3):
        if os.path.isfile(file2):
            f=open(file2, "r")
            dec = f.readlines()
            f.close()

    decoupage = []
    for l in dec:
        l = l.replace(",", " ")
        decoupage.append(l.split())

    idDep = int(decoupage[0][-1])
    nbDecoupages = int(decoupage[1][-1])
    file3="graphe_depts/"+str(num)+".out"

    fdep = open(file3, "r")
    lignes = fdep.readlines()
    fdep.close()

    contenu = []
    for l in lignes:
        l=l.replace(',', ' ')
        contenu.append(l.split())
       
    nbCantons = int(contenu[0][-1])
    popCanton = []
    for i in range(1, nbCantons+1):
        popCanton.append(int(contenu[i][-2]))
    
    return nbDecoupages, decoupage[2:], nbCantons, popCanton


def ecartPop(popCanton, dec, popTotale, nbCircos):
    #print(dec)
    pop = [0]*nbCircos
    for i in range(len(dec)):
        pop[int(dec[i])] += popCanton[i]
    ecartMin = 1
    for i in range(nbCircos):
        ecartMin = min(ecartMin, nbCircos*1.0*pop[i]/popTotale)
    return abs(1-ecartMin)
    
def estExtension(dec, decPartiel):
    dejaPris = set()
    for circo in decPartiel:
        if len(circo) == 0:
            continue

        coulCirco = int(dec[ circo[0]-1 ])
        if coulCirco in dejaPris:
            return False

        for canton in circo:
            if int(dec[canton-1]) != coulCirco:
                return False 
        dejaPris.add(coulCirco)

    return True






def main(num,nb,decPartiel):
    nbCircos = nb[0]
    num=num[0]
    nbDecoupages, decoupage, nbCantons, popCantons = lecture(num)
    popTotale = sum(popCantons)

    ecartMin = 1
    decOpt = []

    for dec in decoupage:
        if estExtension(dec, decPartiel):
            ecart = ecartPop(popCantons, dec[:-nbCircos-1], popTotale, nbCircos)
            if ecart < ecartMin:
                ecartMin = ecart
                decOpt = dec
    return decOpt






entree =[]

num=re.findall(r"[\w']+",sys.argv[1])
num=[int(i) for i in num]
nb=re.findall(r"[\w']+",sys.argv[2])
nb=[int(i) for i in nb]

for i in range(4,12):
    if len(sys.argv)>=i:
        constraint1 = re.findall(r"[\w']+",sys.argv[i-1])
        constraint1 = [int(i) for i in constraint1]
    else:
        break
    entree.append(constraint1)

print(main(num,nb,entree))

# _ = subprocess.call("pdflatex "+str(idFichier)+".tex", shell=True)
# _ = subprocess.call("./convert.py "+str(idFichier)+".pdf", shell=True)
# _ = subprocess.call("rm "+str(idFichier)+".aux "+str(idFichier)+".log "+str(idFichier), shell=True)
