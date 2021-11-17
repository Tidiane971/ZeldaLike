import pygame
from Fonction import *
from constantes import *
from mapgrid import *

def dBox(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 3:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord

biblio = DialogBox(fenetre, x= dBox(1,Home_grid)[0]*64, y = dBox(1,Home_grid)[1]*64, text =["Ce sont des jolies livres", "Qui sont beau", "Tidiane"])

cheminée = DialogBox(fenetre, x=dBox(2,Home_grid)[0]*64, y= dBox(2,Home_grid)[1]*64, text = ["C'est une cheminée. Attention c'est chaud ! "])




DialogBoxes[0][0] = biblio
DialogBoxes[0][1] = cheminée
