import pygame
from constantes import *
from Fonction import *
from mapgrid import *
#Image village

Home_bg = Map(imgHomeBg, fenetre)
Home_front = Map(imgHomeFront, fenetre)

Village_bg = Map(imgVillageBg, fenetre)
Village_front = Map(imgVillageFront, fenetre)

Labyrinthe_bg = Map(imgGrotteBg, fenetre)
Labyrinthe_front = Map(imgGrotteFront, fenetre)

Auberge_bg = Map(imgAubergeBg, fenetre)
Auberge_front = Map(imgAubergeFront, fenetre)


Armurerie_bg = Map(imgArmurerieBg, fenetre)
Armurerie_front = Map(imgArmurerieFront, fenetre)


Boutique_bg = Map(imgBoutiqueBg, fenetre)
Boutique_front = Map(imgBoutiqueFront, fenetre)


Maps = [
[Home_bg,Home_front,Home_grid,(1280,1088)],
[Village_bg,Village_front,Village_grid,(4224,2560)],
[Labyrinthe_bg,Labyrinthe_front, Grotte_grid, (2496,1600)],
[Auberge_bg,Auberge_front,Auberge_grid,(1422,1088)],
[Armurerie_bg,Armurerie_front,Armurerie_grid,(1440,768)],
[Boutique_bg,Boutique_front,Boutique_grid,(1280,960)],

]
actual_map = Maps[0]
