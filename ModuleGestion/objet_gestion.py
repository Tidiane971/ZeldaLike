import pygame
from Graphique.elements_graphique import *
from Utils.constantes import *
from Utils.mapgrid import *



class Objet():
    def __init__(self,image,nom,type):
        self.image = image
        self.nom = nom
        self.type = type



objet_dict = {
    "Potion" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/heal_potion.png"), fenetre), nom = "Une Potion de Heal", type = "consommable"),
    "Mana" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/mana_potion.png"), fenetre), nom = "Une Potion de Mana", type = "consommable"),
    "Clé1" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/key.png"), fenetre), nom = "cle1", type = "quete"),
    "Clé2" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/key.png"), fenetre), nom = "cle2", type = "quete"),
    "Clé3" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/key.png"), fenetre), nom = "cle3", type = "quete"),
    "Collier" : Objet(image = ElementGraphique(pygame.image.load("assets/Source/Autre/collier.png"), fenetre), nom = "collier", type = "quete"),

    }
