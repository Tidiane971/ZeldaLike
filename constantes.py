import pygame
# Définition fenêtre (à changer si besoin)
largeur=840
hauteur=550
fenetre=pygame.display.set_mode((largeur,hauteur))

CameraX=0
CameraY=0
Warps = [[0],[0,0],[0]]


Transi = [pygame.image.load("Source/Transi/1.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/2.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/3.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/4.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/5.jpg").convert_alpha(),
          ]

imgHomeBg = pygame.image.load("Source/Map/home.png").convert_alpha()
imgHomeFront = pygame.image.load("Source/Map/home.png").convert_alpha()

imgVillageBg = pygame.image.load("Source/Map/Village/bg.png").convert_alpha()
imgVillageFront = pygame.image.load("Source/Map/Village/front.png").convert_alpha()

imgVGrotteBg = pygame.image.load("Source/Map/labyrinthe.png").convert_alpha()
imgGrotteFront = pygame.image.load("Source/Map/Village/bg.png").convert_alpha()
