import pygame
import copy
from Graphique.elements_graphique import *

class ComposantInteraction:
    def __init__(self, perso, fenetre):
        self.perso = perso
        self.fenetre = fenetre

    def read(self, DB):
        rectBox = (80, 400)
        boxImage = pygame.image.load("assets/Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715, 144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.perso.rect)

        if touches[pygame.K_s] and not self.perso.pressed:
            self.perso.pressed = True
        if touches[pygame.K_q] and self.perso.inDialog:
            self.perso.pressed = False
            self.perso.inDialog = False

        if self.perso.pressed:
            if self.perso.direction == "stand_haut":
                if self.perso.map[2][(rect_provisoire.y - 64) // 64][(rect_provisoire.x) // 64] == 3:
                    self.perso.inDialog = True
                    rect_provisoire.y -= 64
                    for dialog in DB:
                        for d in dialog:
                            self.perso.inDialog = True
                            self.perso.dialog_lines = d.text[:]  # ou l’équivalent pour PNJ/ coffre

    def talk(self, PNG):
        rectBox = (80, 400)
        boxImage = pygame.image.load("assets/Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715, 144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.perso.rect)

        if touches[pygame.K_s] and not self.perso.pressed:
            self.perso.pressed = True
        if touches[pygame.K_q] and self.perso.inDialog:
            self.perso.pressed = False
            self.perso.inDialog = False

        if self.perso.pressed:
            direction_offsets = {
                "stand_haut": (0, -64),
                "stand_droite": (64, 0),
                "stand_bas": (0, 64),
                "stand_gauche": (-64, 0),
            }
            dx, dy = direction_offsets.get(self.perso.direction, (0, 0))
            rect_provisoire.x += dx
            rect_provisoire.y += dy

            pnj_case = self.perso.map[2][rect_provisoire.y // 64][rect_provisoire.x // 64]

            if pnj_case == 4:
                self.perso.inDialog = True
                for pnj in PNG:
                    for p in pnj:
                        self.perso.inDialog = True
                        self.perso.dialog_lines = p.text[:]  # ou l’équivalent pour PNJ/ coffre

    def open(self, COFFRES):
        rectBox = (80, 400)
        boxImage = pygame.image.load("assets/Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715, 144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.perso.rect)

        if touches[pygame.K_s] and not self.perso.pressed:
            self.perso.pressed = True
        if touches[pygame.K_q] and self.perso.inDialog:
            self.perso.pressed = False
            self.perso.inDialog = False

        if self.perso.pressed:
            direction_offsets = {
                "stand_haut": (0, -64),
                "stand_droite": (64, 0),
                "stand_bas": (0, 64),
                "stand_gauche": (-64, 0),
            }
            dx, dy = direction_offsets.get(self.perso.direction, (0, 0))
            rect_provisoire.x += dx
            rect_provisoire.y += dy

            pnj_case = self.perso.map[2][rect_provisoire.y // 64][rect_provisoire.x // 64]

            if pnj_case == 5:
                for coffre in COFFRES:
                    for c in coffre:
                        if not c.open or self.perso.inDialog:
                            if rect_provisoire.colliderect(c.rect):
                                if not c.open:
                                    self.perso.inventaire.contenu.append(c.objet)
                                    c.open = True

                                    if c.inclinaison == 3:
                                        c.image = pygame.image.load("assets/Source/Autre/Chest/chest_open_bas.png")
                                        c.image = pygame.transform.scale(c.image, (60, 60))

                                self.perso.inDialog = True
                                self.perso.dialog_lines = [f"Vous avez trouvé {c.objet.nom} !"]

