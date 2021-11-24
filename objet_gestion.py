import pygame
from Fonction import *
from constantes import *
from mapgrid import *



objet_dict = {
    "Potion" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/heal_potion.png"), fenetre), nom = "Une Potion de Heal", type = "consommable"),
    "Mana" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/mana_potion.png"), fenetre), nom = "Une Potion de Mana", type = "consommable"),
    "Clé1" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/key.png"), fenetre), nom = "cle1", type = "quete"),
    "Clé2" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/key.png"), fenetre), nom = "cle2", type = "quete"),
    "Clé3" : Objet(image = elementgraphique(pygame.image.load("Source/Autre/key.png"), fenetre), nom = "cle3", type = "quete"),

    }
