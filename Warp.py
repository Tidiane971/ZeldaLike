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

home_entree = Warp(fenetre, x=wWarp(3,Village_grid)[0]*64, y = wWarp(3, Village_grid)[1]*64, inclinaison=3, destination = [0,0], lock = False)
home_sortie = Warp(fenetre, x=wWarp(1,Home_grid)[0]*64, y = wWarp(1, Home_grid)[1]*64, inclinaison=1, destination = [1,2], lock = False)


grotte_entree = Warp(fenetre,x=wWarp(2,Village_grid)[0]*64,y=wWarp(2,Village_grid)[1]*64,inclinaison=3,destination = [2,0],lock=False)
grotte_sortie = Warp(fenetre,x=wWarp(1,Grotte_grid)[0]*64,y=wWarp(1,Grotte_grid)[1]*64+150,inclinaison=1,destination = [1,1] , lock=False)

auberge_entree = Warp(fenetre,x=wWarp(1,Village_grid)[0]*64,y=wWarp(1,Village_grid)[1]*64,inclinaison=3,destination = [3,0],lock=False)
auberge_sortie = Warp(fenetre,x=wWarp(1,Auberge_grid)[0]*64,y=wWarp(1,Auberge_grid)[1]*64,inclinaison=1,destination = [1,0] , lock=False)

armurerie_entree = Warp(fenetre,x=wWarp(5,Village_grid)[0]*64,y=wWarp(5,Village_grid)[1]*64,inclinaison=3,destination = [4,0],lock=False)
armurerie_sortie = Warp(fenetre,x=wWarp(1,Armurerie_grid)[0]*64,y=wWarp(1,Armurerie_grid)[1]*64,inclinaison=1,destination = [1,4] , lock=False)

boutique_entree = Warp(fenetre,x=wWarp(6,Village_grid)[0]*64,y=wWarp(6,Village_grid)[1]*64,inclinaison=3,destination = [5,0],lock=False)
boutique_sortie = Warp(fenetre,x=wWarp(1,Boutique_grid)[0]*64,y=wWarp(1,Boutique_grid)[1]*64,inclinaison=1,destination = [1,5] , lock=False)

witch_entree = Warp(fenetre,x=wWarp(4,Village_grid)[0]*64,y=wWarp(4,Village_grid)[1]*64,inclinaison=3,destination = [6,0],lock=False)
witch_sortie = Warp(fenetre,x=wWarp(1,Witch_grid)[0]*64,y=wWarp(1,Witch_grid)[1]*64,inclinaison=1,destination = [1,3] , lock=False)


Warps[1][2] =  home_entree
Warps[0][0] = home_sortie

Warps[1][1] = grotte_entree
Warps[2][0] = grotte_sortie

Warps[1][0] = auberge_entree
Warps[3][0] = auberge_sortie


Warps[1][4] = armurerie_entree
Warps[4][0] = armurerie_sortie

Warps[1][5] = boutique_entree
Warps[5][0] = boutique_sortie

Warps[1][3] = witch_entree
Warps[6][0] = witch_sortie
