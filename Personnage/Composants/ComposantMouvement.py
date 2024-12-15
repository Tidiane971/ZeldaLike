import copy
import pygame

class ComposantMouvement:
    def __init__(self, vitesse=9):
        self.vitesse = vitesse
        self.direction = "stand_bas"
        self.delai = 3
        self.timer = 0

    def move(self, rect, touches, map_data, largeur, hauteur, camerax, cameray, vie):
        rect_provisoire = copy.copy(rect)

        # Déplacement basé sur les touches
        if vie != 0 and touches[pygame.K_LEFT]:
            self.delai = 1
            self.direction = "gauche"
            rect_provisoire.x -= self.vitesse
        elif vie != 0 and self.direction == "gauche":
            self.direction = "stand_gauche"
            self.delai = 3

        if vie != 0 and touches[pygame.K_RIGHT]:
            self.delai = 1
            self.direction = "droite"
            rect_provisoire.x += self.vitesse
        elif vie != 0 and self.direction == "droite":
            self.direction = "stand_droite"
            self.delai = 3

        if vie != 0 and touches[pygame.K_UP]:
            self.delai = 1.5
            self.direction = "haut"
            rect_provisoire.y -= self.vitesse
        elif vie != 0 and self.direction == "haut":
            self.direction = "stand_haut"
            self.delai = 3

        if vie != 0 and touches[pygame.K_DOWN]:
            self.delai = 1.5
            self.direction = "bas"
            rect_provisoire.y += self.vitesse
        elif vie != 0 and self.direction == "bas":
            self.direction = "stand_bas"
            self.delai = 3

        # Vérification des collisions
        if (map_data[2][rect_provisoire.y // 64][rect_provisoire.x // 64] == 0 and
            map_data[2][rect_provisoire.y // 64][(rect_provisoire.x + 52) // 64] == 0 and
            map_data[2][(rect_provisoire.y + 52) // 64][rect_provisoire.x // 64] == 0 and
            map_data[2][(rect_provisoire.y + 52) // 64][(rect_provisoire.x + 52) // 64] == 0):

            rect = rect_provisoire
            camerax = rect.x - (largeur // 2)
            cameray = rect.y - (hauteur // 2)

        # Gestion des limites de la carte et de la caméra
        if rect.x < 0:
            rect.x = 0
        elif rect.y < 0:
            rect.y = 0

        limitex, limitey = map_data[3]
        if cameray < 0:
            cameray = 0
        if camerax < 0:
            camerax = 0
        if camerax > limitex - largeur:
            camerax = limitex - largeur
        if cameray > limitey - hauteur:
            cameray = limitey - hauteur

        return rect, camerax, cameray
    