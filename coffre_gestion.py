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

map3_coffre1 = coffre(fenetre,image = pygame.image.load("Source/Autre/Chest/big_chest_bas.png") ,x= dBox(1,Grotte_grid)[0]*64, y = dBox(1,Grotte_grid)[1]*64,objet = objet_dict["Mana"], inclinaison = 3, open = False)

coffre_liste[0][0] = map1_coffre_1
coffre_liste[1][0] = map2_coffre_1
coffre_liste[2][0] = map3_coffre1
