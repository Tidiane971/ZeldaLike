import pygame
from Graphique.elements_graphique import *
from Utils.constantes import *
from Utils.mapgrid import *
from ModuleGestion.objet_gestion import *
from Ennemi.ennemi import Ennemi, EnemyType
from Graphique.chargeur_object import * 
from Ennemi.EnemyLifeObserver import EnemyLifeObserver


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

# Définir des EnemyType
korogu_type = EnemyType(objet["ennemi"]["korogu"], vie=4, vitesse=9)
boss_type = EnemyType(objet["ennemi"]["boss"], vie=20, vitesse=4)

ennemi_grotte_1 = Ennemi(korogu_type, fenetre,x=dBox(1,Grotte_grid)[0]*64 ,y=dBox(1,Grotte_grid)[1]*64, direction ="gauche")
ennemi_grotte_2 = Ennemi(korogu_type, fenetre,x=dBox(2,Grotte_grid)[0]*64 ,y=dBox(2,Grotte_grid)[1]*64, direction ="gauche")
ennemi_grotte_3 = Ennemi(korogu_type, fenetre,x=dBox(3,Grotte_grid)[0]*64 ,y=dBox(3,Grotte_grid)[1]*64, direction ="gauche")
ennemi_grotte_4 = Ennemi(korogu_type, fenetre,x=dBox(4,Grotte_grid)[0]*64 ,y=dBox(4,Grotte_grid)[1]*64, direction ="gauche")


# ... création des ennemis

ennemi_grotte_1.attach(EnemyLifeObserver())
ennemi_grotte_2.attach(EnemyLifeObserver())
ennemi_grotte_3.attach(EnemyLifeObserver())
ennemi_grotte_4.attach(EnemyLifeObserver())

boss = Ennemi(boss_type, fenetre,x=dBox(1,Salle_boss_grid)[0]*64 ,y=dBox(1,Salle_boss_grid)[1]*64, direction ="gauche")

ennemi_liste[2][0] = ennemi_grotte_1
ennemi_liste[2][1] = ennemi_grotte_2
ennemi_liste[2][2] = ennemi_grotte_3
ennemi_liste[2][3] = ennemi_grotte_4

ennemi_liste[6][0] = boss
