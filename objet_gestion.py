import pygame
from Fonction import *
from constantes import *
from mapgrid import *



objet_dict = {
    "Potion" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/heal_potion.png"), fenetre), nom = "Une Potion de Heal", type = "consommable"),

    "Mana" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/mana_potion.png"), fenetre), nom = "Une Potion de Mana", type = "consommable"),
    }
