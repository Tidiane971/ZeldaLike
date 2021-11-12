import pygame
from constantes import *
from Fonction import elementgraphique

#Image village
Village = pygame.image.load("bg.jpg").convert_alpha()
Village = pygame.transform.scale(Village, (2520,1650))
Village = elementgraphique(Village, fenetre)