#!/usr/bin/env python

#nomFichierEntree = "dessins/sortie63-0001pour100.txt"#input()
#nbCircos = 3#int(input())
import json 
import subprocess
import sys
import re


def lecture():
    f = open("sortie01.txt", "r")
    dec = f.readlines()
    f.close()
    
    decoupage = []
    for l in dec:
        l = l.replace(",", " ")
        decoupage.append(l.split())

    idDep = int(decoupage[0][-1])
    nbDecoupages = int(decoupage[1][-1])

    fdep = open("1.out", "r")
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

        coulCirco = int(dec[ circo[0] ])
        if coulCirco in dejaPris:
            return False

        for canton in circo:
            if int(dec[canton]) != coulCirco:
                return False 
        dejaPris.add(coulCirco)

    return True



def printCanton(pts, couleur, tex):
    tex.write("\\draw[fill="+couleur+"] \n")
    for idPoint in range(len(pts)):
        tex.write( "(" + str(pts[idPoint][0]) + "," + str( pts[idPoint][1]) + ") --")
    tex.write( " cycle;\n")



def main(decPartiel):
    couleurs = ["blue", "red", "green"]
    

    nbCircos = 3
    nbDecoupages, decoupage, nbCantons, popCantons = lecture()
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
    # tex = open(str(idF)+".tex", "w")
    # tex.write( "\\documentclass[10pt]{article} \n \\usepackage{tikz}\n \\begin{document}\n")
    
    # if(decOpt == []):
    #     tex.write("\\section{Pas d'extension valide} \n \\end{document}\n")

    # else:
    #     nbC = len(cantons)
        
    #     tex.write("\\begin{figure} \n \centering \n \caption{Ecart a la moyenne : " + str(ecartMin) + "}\n")
    #     tex.write( "\\begin{tikzpicture}[scale=6,yscale=1.2] \n")
    #     for idC in range(nbC): 
    #         c = int(decOpt[idC])
    #         if(cantons[idC]["geometry"]["type"] == "MultiPolygon"):
    #             for idP in range(len(cantons[idc]["geometry"]["coordinates"])):
    #                 printCanton(cantons[idC]["geometry"]["coordinates"][idP][0], couleurs[c], tex)
    #         else:
    #             printCanton(cantons[idC]["geometry"]["coordinates"][0], couleurs[c], tex)
    #     tex.write("\\end{tikzpicture}\n \\end{figure} \n \\bigskip\n \\end{document}\n")
    
    # tex.close()




# idFichier = sys.argv[1]
# f = open(idFichier, "r")
# lines = f.readlines()
# f.close()
if len(sys.argv)>=2:
    constraint1 = re.findall(r"[\w']+",sys.argv[1])
    constraint1 = [int(i) for i in constraint1]
else:
    constraint1 =[]
if len(sys.argv)>=3:
    constraint2 = re.findall(r"[\w']+",sys.argv[2])
    constraint2 = [int(i) for i in constraint1]
else:
    constraint2 =[]
if len(sys.argv)>=4:
    constraint3 = re.findall(r"[\w']+",sys.argv[3])
    constraint3 = [int(i) for i in constraint1]
else:
    constraint3 =[]





# constraint2 = re.findall(r"[\w']+",sys.argv[2])
# constraint3 = re.findall(r"[\w']+",sys.argv[3])
# # constraint1 = sys.argv[1]
# # constraint2 = sys.argv[2]
# # constraint3 = sys.argv[3]


# constraint2 = [int(i) for i in constraint2]
# constraint3 = [int(i) for i in constraint3]

    
entree = [constraint1, constraint2, constraint3]

print(main(entree))

# _ = subprocess.call("pdflatex "+str(idFichier)+".tex", shell=True)
# _ = subprocess.call("./convert.py "+str(idFichier)+".pdf", shell=True)
# _ = subprocess.call("rm "+str(idFichier)+".aux "+str(idFichier)+".log "+str(idFichier), shell=True)
