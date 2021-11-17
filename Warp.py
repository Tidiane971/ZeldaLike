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


home_sortie = Warp(fenetre, x=wWarp(1,Home_grid)[0]*64, y = wWarp(1, Home_grid)[1]*64, inclinaison=1, destination = [1,1], lock = False)
home_entree = Warp(fenetre, x=wWarp(2,Village_grid)[0]*64, y = wWarp(2, Village_grid)[1]*64, inclinaison=3, destination = [0,0], lock = False)
grotte_entree = Warp(fenetre,x=wWarp(1,Village_grid)[0]*64,y=wWarp(1,Village_grid)[1]*64,inclinaison=3,destination = [2,0],lock=False)
grotte_sortie = Warp(fenetre,x=wWarp(1,Grotte_grid)[0]*64,y=wWarp(1,Grotte_grid)[1]*64,inclinaison=1,destination = [1,0] , lock=False)

Warps[0][0] = home_sortie
Warps[1][0] = grotte_entree
Warps[1][1] =  home_entree
Warps[2][0] = grotte_sortie
