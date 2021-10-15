import pygame
from Fonction import *
from Map import *
from constantes import *

#CREATION DE L'IMAGE DE FOND
background_img = pygame.image.load("MENU/background.jpg").convert_alpha()
background_img = pygame.transform.scale(background_img, (largeur,hauteur))
menu_background = elementgraphique(background_img, fenetre)

#CREATION DU BOUTON PLAY DU Menu
play_button_img = pygame.image.load("MENU/playBTN.png").convert_alpha()
play_button_img = pygame.transform.scale(play_button_img,(600,400))
play_button = button(play_button_img,fenetre)
play_button.rect.x = 100
play_button.rect.y = 80
