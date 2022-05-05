import pygame
from Fonction import *
from constantes import *
from mapgrid import *
from objet_gestion import *
def dBox(num, T):
    coord = [0,0]
    k=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 5:
                k+=1
                if k == num:
                    coord[0] = j
                    coord[1] = i
                    return coord


map1_coffre_1 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(1,Home_grid)[0]*64, y = dBox(1,Home_grid)[1]*64,objet = objet_dict["Potion"], inclinaison = 3, open = False)

map2_coffre_1 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(1,Village_grid)[0]*64, y = dBox(1,Village_grid)[1]*64,objet = objet_dict["Potion"], inclinaison = 3, open = False)

map2_coffre_2 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(2,Village_grid)[0]*64, y = dBox(2,Village_grid)[1]*64,objet = objet_dict["Mana"], inclinaison = 3, open = False)

map3_coffre_1 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(1,Grotte_grid)[0]*64, y = dBox(1,Grotte_grid)[1]*64,objet = objet_dict["Clé1"], inclinaison = 3, open = False)

map3_coffre_2 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(2,Grotte_grid)[0]*64, y = dBox(2,Grotte_grid)[1]*64,objet = objet_dict["Clé2"], inclinaison = 3, open = False)

map3_coffre_3 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(3,Grotte_grid)[0]*64, y = dBox(3,Grotte_grid)[1]*64,objet = objet_dict["Clé3"], inclinaison = 3, open = False)

map6_coffre_1 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(1,Salle_boss_grid)[0]*64, y = dBox(1,Salle_boss_grid)[1]*64,objet = objet_dict["Collier"], inclinaison = 3, open = False)


coffre_liste[0][0] = map1_coffre_1

coffre_liste[1][0] = map2_coffre_1
coffre_liste[1][1] = map2_coffre_2

coffre_liste[2][0] = map3_coffre_1
coffre_liste[2][1] = map3_coffre_2
coffre_liste[2][2] = map3_coffre_3

coffre_liste[6][0] = map6_coffre_1
