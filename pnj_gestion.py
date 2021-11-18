import pygame
from Fonction import *
from constantes import *
from mapgrid import *

def dBox(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 4:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord


papi = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/Papi_stand_bas.png") ,x= dBox(1,Home_grid)[0]*64, y = dBox(1,Home_grid)[1]*64,text = ["Bonjour jeune homme"], inclinaison = 3)

pnj_liste[0][0] = papi
