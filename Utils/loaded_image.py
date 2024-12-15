import pygame
from Utils.constantes import *

#CREATION DE L'IMAGE D'INTRO
background_intro = pygame.image.load("assets/Source/Menu/TiMaWy.png").convert_alpha()
background_intro = pygame.transform.scale(background_intro, (largeur,hauteur))


noir = pygame.image.load("assets/Source/Menu/FondNoir.png").convert_alpha()
noir = pygame.transform.scale(noir, (largeur,hauteur))


#CREATION DE L'IMAGE DE FOND
background_img = pygame.image.load("assets/Source/Menu/Menu.png").convert_alpha()
background_img = pygame.transform.scale(background_img, (largeur,hauteur))


#CREATION DU texte PLAY DU MENU
play_button_img = pygame.image.load("assets/Source/Menu/playTXT.png").convert_alpha()
play_button_img = pygame.transform.scale(play_button_img,(600,400))


#CREATION DES IMAGES DE PAUSE
pause1 = pygame.image.load("assets/Source/Autre/pause1.png").convert_alpha()
pause1 = pygame.transform.scale(pause1, (largeur,hauteur))

pause2 = pygame.image.load("assets/Source/Autre/pause2.png").convert_alpha()
pause2 = pygame.transform.scale(pause2, (largeur,hauteur))

#CREATION IMAGES GAME OVER
gameover = pygame.image.load("assets/Source/Autre/GameOver.png").convert_alpha()
gameover = pygame.transform.scale(gameover, (largeur,hauteur))


gameover2 = pygame.image.load("assets/Source/Autre/GameOver2.png").convert_alpha()
gameover2 = pygame.transform.scale(gameover2, (largeur,hauteur))

Transi = [pygame.image.load("assets/Source/Transi/1.jpg").convert_alpha(),
          pygame.image.load("assets/Source/Transi/2.jpg").convert_alpha(),
          pygame.image.load("assets/Source/Transi/3.jpg").convert_alpha(),
          pygame.image.load("assets/Source/Transi/4.jpg").convert_alpha(),
          pygame.image.load("assets/Source/Transi/5.jpg").convert_alpha(),
          ]

imgHomeBg = pygame.image.load("assets/Source/Map/home.png").convert_alpha()
imgHomeFront = pygame.image.load("assets/Source/Map/home_front.png").convert_alpha()

imgVillageBg = pygame.image.load("assets/Source/Map/Village/bg.png").convert_alpha()
imgVillageFront = pygame.image.load("assets/Source/Map/Village/front.png").convert_alpha()

imgGrotteBg = pygame.image.load("assets/Source/Map/dungeon.png").convert_alpha()
imgGrotteFront = pygame.image.load("assets/Source/Map/warp.png").convert_alpha()


imgAubergeBg = pygame.image.load("assets/Source/Map/auberge.png").convert_alpha()
imgAubergeFront = pygame.image.load("assets/Source/Map/auberge_font.png").convert_alpha()


imgArmurerieBg = pygame.image.load("assets/Source/Map/weapon_shop.png").convert_alpha()
imgArmurerieFront = pygame.image.load("assets/Source/Map/weapon_shop_front.png").convert_alpha()


imgBoutiqueBg = pygame.image.load("assets/Source/Map/boutique.png").convert_alpha()
imgBoutiqueFront = pygame.image.load("assets/Source/Map/boutique_front.png").convert_alpha()

imgBossBg = pygame.image.load("assets/Source/Map/Salle_Boss.png").convert_alpha()
imgBossFront = pygame.image.load("assets/Source/Map/warp.png").convert_alpha()
