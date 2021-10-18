import pygame
from constantes import *
from Fonction import elementgraphique

#Image village
Village = pygame.image.load("bg.jpg").convert_alpha()
Village = pygame.transform.scale(Village, (largeur,hauteur))
Village = elementgraphique(Village, fenetre)