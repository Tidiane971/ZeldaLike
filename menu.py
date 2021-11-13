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

#CREATION DE L'IMAGE GAME OVER
gameover = pygame.image.load("Source/Autre/GameOver.png").convert_alpha()
gameover = pygame.transform.scale(gameover, (largeur,hauteur))
GAMEOVER = elementgraphique(gameover, fenetre)
