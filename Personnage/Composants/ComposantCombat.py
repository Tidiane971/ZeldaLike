import pygame
import copy

class ComposantCombat:
    def __init__(self, perso):
        self.perso = perso  # Référence au personnage pour accéder à ses propriétés
        self.b = 0  # Timer pour la gestion de l'invincibilité des ennemis

    def attack(self, touches, ennemiL, map_having_ennemi):
        if not touches[pygame.K_a]:
            return  # Pas d'attaque

        direction_map = {
            "stand_bas": (0, 64, "hit_bas"),
            "bas": (0, 64, "hit_bas"),
            "stand_haut": (0, -64, "hit_haut"),
            "haut": (0, -64, "hit_haut"),
            "stand_gauche": (-64, 0, "hit_gauche"),
            "gauche": (-64, 0, "hit_gauche"),
            "stand_droite": (64, 0, "hit_droite"),
            "droite": (64, 0, "hit_droite"),
        }

        if self.perso.direction not in direction_map:
            return  # Direction invalide pour une attaque

        dx, dy, attack_direction = direction_map[self.perso.direction]

        # Met à jour l'état de l'attaque
        self.perso.delai = 1
        self.perso.attak = attack_direction
        self.perso.direction = attack_direction
        self.perso.attak_fin = False

        # Crée le rectangle d'attaque
        attack_rect = copy.copy(self.perso.rect)
        attack_rect.x += dx
        attack_rect.y += dy

        # Vérifie les collisions avec les ennemis
        if self.perso.map[2][attack_rect.y // 64][attack_rect.x // 64] == 6:
            if self.perso.map_id in map_having_ennemi:
                for ennemi in ennemiL:
                    if attack_rect.colliderect(ennemi.rect) and not ennemi.invincible:
                        ennemi.vie -= 4
                        self.b = pygame.time.get_ticks()
                        ennemi.invincible = True
                        print(f"Ennemi touché ! Vie restante : {ennemi.vie}")

        # Gestion de l'invincibilité des ennemis
        for ennemi in ennemiL:
            if ennemi.invincible:
                ennemi.image = pygame.image.load("assets/Source/Map/warp.png")
                if pygame.time.get_ticks() - self.b > 2500:
                    ennemi.invincible = False
