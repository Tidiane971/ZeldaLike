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
ennemi_grotte_2 = ennemi(objet["ennemi"]["korogu"],fenetre,x=dBox(2,Grotte_grid)[0]*64 ,y=dBox(2,Grotte_grid)[1]*64,perso=perso, dir = "gauche")
ennemi_grotte_3 = ennemi(objet["ennemi"]["korogu"],fenetre,x=dBox(3,Grotte_grid)[0]*64 ,y=dBox(3,Grotte_grid)[1]*64,perso=perso, dir = "gauche")
ennemi_grotte_4 = ennemi(objet["ennemi"]["korogu"],fenetre,x=dBox(4,Grotte_grid)[0]*64 ,y=dBox(4,Grotte_grid)[1]*64,perso=perso, dir = "gauche")
ennemi_grotte_5 = ennemi(objet["ennemi"]["korogu"],fenetre,x=dBox(5,Grotte_grid)[0]*64 ,y=dBox(5,Grotte_grid)[1]*64,perso=perso, dir = "gauche")

boss = ennemi(objet["ennemi"]["boss"],fenetre,x=dBox(1,Salle_boss_grid)[0]*64 ,y=dBox(1,Salle_boss_grid)[1]*64,perso=perso, dir = "gauche")

ennemi_liste[2][0] = ennemi_grotte_1
ennemi_liste[2][1] = ennemi_grotte_2
ennemi_liste[2][2] = ennemi_grotte_3
ennemi_liste[2][3] = ennemi_grotte_4
ennemi_liste[2][4] = ennemi_grotte_5

ennemi_liste[6][0] = boss
ennemi_liste[6][0].vie = 30
