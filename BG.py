import pygame
from Fonction import *
from constantes import *

#CREATION DE L'IMAGE D'INTRO
background_intro = pygame.image.load("Source/Menu/TiMaWy.png").convert_alpha()
background_intro = pygame.transform.scale(background_intro, (largeur,hauteur))
intro_background = elementgraphique(background_intro, fenetre)

#CREATION DE L'IMAGE DE FOND
background_img = pygame.image.load("Source/Menu/Menu.png").convert_alpha()
background_img = pygame.transform.scale(background_img, (largeur,hauteur))
menu_background = elementgraphique(background_img, fenetre)

#CREATION DU BOUTON PLAY DU MENU
#play_button_img = pygame.image.load("Source/Menu/playBTN.png").convert_alpha()
#play_button_img = pygame.transform.scale(play_button_img,(600,400))
#play_button = button(play_button_img,fenetre)
#play_button.rect.x = 100
#play_button.rect.y = 80

#CREATION DU texte PLAY DU MENU
play_button_img = pygame.image.load("Source/Menu/playTXT.png").convert_alpha()
play_button_img = pygame.transform.scale(play_button_img,(600,400))
play_button = button(play_button_img,fenetre)
play_button.rect.x = 135
play_button.rect.y = 95

#CREATION DES IMAGES DE PAUSE
pause1 = pygame.image.load("Source/Autre/pause1.png").convert_alpha()
pause1 = pygame.transform.scale(pause1, (largeur,hauteur))
Pause1 = elementgraphique(pause1, fenetre)

pause2 = pygame.image.load("Source/Autre/pause2.png").convert_alpha()
pause2 = pygame.transform.scale(pause2, (largeur,hauteur))
Pause2 = elementgraphique(pause2, fenetre)

#CREATION DE L'IMAGE GAME OVER
gameover = pygame.image.load("Source/Autre/GameOver.png").convert_alpha()
gameover = pygame.transform.scale(gameover, (largeur,hauteur))
GAMEOVER = elementgraphique(gameover, fenetre)
