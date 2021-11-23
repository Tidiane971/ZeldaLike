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

armurier = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/Male7_stand_bas.png") ,x= dBox(1,Armurerie_grid)[0]*64, y = dBox(1,Armurerie_grid)[1]*64,text = ["Voulez-vous une épée ?"], inclinaison = 3)

epiciere = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/Fille5_stand_bas.png") ,x= dBox(1,Boutique_grid)[0]*64, y = dBox(1,Boutique_grid)[1]*64,text = ["Un thé, jeune homme ?"], inclinaison = 3)

aubergiste = pnj(fenetre,image = pygame.image.load("Source/PNJ/USE/Male8_stand_bas.png") ,x= dBox(1,Auberge_grid)[0]*64, y = dBox(1,Auberge_grid)[1]*64,text = ["Vous cherchez un endroit ou vousr reposer ?"], inclinaison = 3)


pnj_liste[0][0] = papi
pnj_liste[3][0] = aubergiste
pnj_liste[4][0] = armurier
pnj_liste[5][0] = epiciere
