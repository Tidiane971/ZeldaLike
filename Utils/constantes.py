import pygame
import pygame.freetype

pygame.init()
# Définition fenêtre (à changer si besoin)
largeur=840
hauteur=550
fenetre=pygame.display.set_mode((largeur,hauteur))

CameraX=0
CameraY=0

DialogBoxes = [ [0,0],[], [] ,[], [], [], []]
coffre_liste = [ [0],[0,0],[0,0,0],[],[],[],[0]]
ennemi_liste = [ [],[], [0,0,0,0] ,[], [], [], [0]]
pnj_liste = [
    [None],          # map 0, 1 PNJ
    [None, None, None, None, None],  # map 1, 5 PNJ
    [],              # map 2, pas de PNJ
    [None],          # map 3, 1 PNJ
    [None],          # map 4, 1 PNJ
    [None],          # map 5, 1 PNJ
    []               # map 6, pas de PNJ
]


Intro, Menu, enJeu, GameOver = 1,0,0,0
myfont = pygame.freetype.Font(None, 15)
map_having_pnj = [0,1,3,4,5]
map_having_coffre = [0,1,2,6]
map_having_ennemi = [2,6]


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

