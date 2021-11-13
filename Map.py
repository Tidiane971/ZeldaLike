import pygame
from constantes import *


#Image village
Village = pygame.image.load("Source/Map/bonbg.png").convert_alpha()
Village_rect = Village.get_rect()
Village_rect.x = 0
Village_rect.y = 0
CameraX=0
CameraY=0