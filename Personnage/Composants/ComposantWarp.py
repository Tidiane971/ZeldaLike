import time
import pygame
import copy

class ComposantWarping:

    def __init__(self, perso, fenetre):
        self.perso = perso  # Reference to the player for accessing attributes
        self.fenetre = fenetre  # The game window for rendering

    def warp(self, objet_dict, Transi):
    
        rect_provisoire = copy.copy(self.perso.rect)
        warp_case = 0

        # Determine warp direction
        direction_offsets = {
            "haut": (0, -64),
            "droite": (64, 0),
            "bas": (0, 64),
            "gauche": (-64, 0)
        }

        if self.perso.direction in direction_offsets:
            dx, dy = direction_offsets[self.perso.direction]
            warp_case = self.perso.map[2][(rect_provisoire.y + dy + 52) // 64][(rect_provisoire.x + dx) // 64]
            rect_provisoire.x += dx
            rect_provisoire.y += dy

        if int(str(warp_case)[0]) == 2:
            self.handle_warp(warp_case, objet_dict, Transi)

    def handle_warp(self, warp_case, objet_dict, Transi):
        largeur, hauteur = self.fenetre.get_size()

        # Check if warp requires a key
        if len(str(warp_case)) < 8 or any(objet_dict[key] in self.perso.inventaire.contenu for key in ["Clé1", "Clé2", "Clé3"]):
            # Execute transition
            for fondu in Transi:
                self.fenetre.blit(fondu, (0, 0))
                pygame.display.flip()
                time.sleep(0.05)

            # Update map and player position
            self.perso.map_id = int(str(warp_case)[1])
            self.perso.rect.x = int(str(warp_case)[2:4]) * 64
            self.perso.rect.y = int(str(warp_case)[4:6]) * 64
            inclinaison = int(str(warp_case)[6])

            # Adjust player position based on inclinaison
            if inclinaison == 1:
                self.perso.rect.y -= 64
            elif inclinaison == 2:
                self.perso.rect.x += 64
            elif inclinaison == 3:
                self.perso.rect.y += 64
            elif inclinaison == 4:
                self.perso.rect.x -= 64

            # Update camera
            self.perso.camerax = self.perso.rect.x - (largeur // 2)
            self.perso.cameray = self.perso.rect.y - (hauteur // 2)


