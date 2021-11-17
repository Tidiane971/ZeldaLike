import pygame
from constantes import *
from Fonction import *
from mapgrid import *
#Image village

Home_bg = Map(imgHomeBg, fenetre)
Home_front = Map(imgHomeFront, fenetre)

Village_bg = Map(imgVillageBg, fenetre)
Village_front = Map(imgVillageFront, fenetre)

Labyrinthe_bg = Map(imgVGrotteBg, fenetre)
Labyrinthe_front = Map(imgGrotteFront, fenetre)

Maps = [[Home_bg,Home_front,Home_grid,(1280,1088)],[Village_bg,Village_front,Village_grid,(5056,3264)], [Labyrinthe_bg,Labyrinthe_front,Grotte_grid,(2496,1600)]]
actual_map = Maps[0]
