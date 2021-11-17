import pygame
from Fonction import *
from constantes import *
from mapgrid import *

def wWarp(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 2:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord



grotte_entree = Warp(fenetre,x=wWarp(1,T)[0]*64,y=wWarp(1,T)[1]*64,inclinaison=3,destination = [1,0],lock=False)
grotte_sortie = Warp(fenetre,x=wWarp(1,L)[0]*64,y=wWarp(1,L)[1]*64,inclinaison=3,destination = [0,0] , lock=False)

Warps[0][0] = grotte_entree
Warps[1][0] = grotte_sortie


def wWarp(num, T):
    coord = []
    i=0
    for i in T:
        for j in T[i]:
            if j == 2:
                i+=1
                if i == num:
                    coord[0] = j
                    coord[1] = i
                    return coord
