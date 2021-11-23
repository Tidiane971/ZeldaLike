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
pnj_liste = [ [0],[],[],[0],[0],[0],[] ]
coffre_liste = [ [0],[0,0],[],[],[],[],[]]
ennemi_liste = [ [],[], [0] ,[], [], [], []]


Intro, Menu, enJeu, GameOver = 1,0,0,0
myfont = pygame.freetype.Font(None, 15)
map_having_pnj = [0,3,4,5]
map_having_coffre = [0,1]
map_having_ennemi = [2]

Transi = [pygame.image.load("Source/Transi/1.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/2.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/3.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/4.jpg").convert_alpha(),
          pygame.image.load("Source/Transi/5.jpg").convert_alpha(),
          ]

imgHomeBg = pygame.image.load("Source/Map/home.png").convert_alpha()
imgHomeFront = pygame.image.load("Source/Map/home_front.png").convert_alpha()

imgVillageBg = pygame.image.load("Source/Map/Village/bg.png").convert_alpha()
imgVillageFront = pygame.image.load("Source/Map/warp.png").convert_alpha()

imgGrotteBg = pygame.image.load("Source/Map/dungeon.png").convert_alpha()
imgGrotteFront = pygame.image.load("Source/Map/warp.png").convert_alpha()


imgAubergeBg = pygame.image.load("Source/Map/auberge.png").convert_alpha()
imgAubergeFront = pygame.image.load("Source/Map/auberge_font.png").convert_alpha()


imgArmurerieBg = pygame.image.load("Source/Map/weapon_shop.png").convert_alpha()
imgArmurerieFront = pygame.image.load("Source/Map/weapon_shop_front.png").convert_alpha()


imgBoutiqueBg = pygame.image.load("Source/Map/boutique.png").convert_alpha()
imgBoutiqueFront = pygame.image.load("Source/Map/boutique_front.png").convert_alpha()

imgBossBg = pygame.image.load("Source/Map/Salle_Boss.png").convert_alpha()
imgBossFront = pygame.image.load("Source/Map/warp.png").convert_alpha()
