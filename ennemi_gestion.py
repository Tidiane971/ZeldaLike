import pygame
from Fonction import *
from constantes import *
from mapgrid import *
from objet_gestion import *
objet = lecture_objet()
def dBox(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 6:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord


ennemi_grotte_1 = ennemi(objet["ennemi"]["korogu"],fenetre,x=dBox(1,Grotte_grid)[0]*64 ,y=dBox(1,Grotte_grid)[1]*64,perso=perso, dir = "gauche")
# Grotte_grid[ennemi_grotte_1.rect.y//64][ennemi_grotte_1.rect.x//64] = 0;
ennemi_liste[2][0] = ennemi_grotte_1
