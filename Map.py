import pygame
from constantes import *
from Fonction import *
from mapgrid import *
#Image village


Village_bg = Map(pygame.image.load("Source/Map/Village/bg.png").convert_alpha(), fenetre)
Village_front = Map(pygame.image.load("Source/Map/Village/front.png").convert_alpha(), fenetre)

Labyrinthe_bg = Map(pygame.image.load("Source/Map/labyrinthe.png").convert_alpha(), fenetre)
Labyrinthe_front = Map(pygame.image.load("Source/Map/Village/front.png").convert_alpha(), fenetre)

Maps = [[Village_bg,Village_front,T], [Labyrinthe_bg,Labyrinthe_front,L]]
actual_map = Maps[0]
