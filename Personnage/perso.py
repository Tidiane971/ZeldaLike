from Graphique.elements_graphique import *
from inventaire import Inventaire
from Graphique.animation import *
from Personnage.Composants.ComposantWarp import ComposantWarping
from Personnage.Composants.ComposantCombat import ComposantCombat
from Personnage.Composants.ComposantMouvement import ComposantMouvement
from Personnage.Composants.ComposantInteraction import ComposantInteraction
import pygame

# Import patterns
from Personnage.fsm_perso import FSM
from patterns import Subject

class Perso(element_anime_dir, Subject):
    def __init__(self, image, fenetre, camerax, cameray, map, map_id, x=0, y=0):
        element_anime_dir.__init__(self, image, fenetre, x, y)
        Subject.__init__(self)  # Initialiser le Subject

        self.vie = 12
        self.vitesse = 9
        self.attak_fin = True
        self.attak = ""
        self.camerax = camerax
        self.cameray = cameray
        self.map = map
        self.map_id = map_id
        self.fenetre = fenetre
        self.inDialog = False
        self.pressed = False
        self.inventaire = Inventaire(fenetre=self.fenetre, perso=self)
        self.invincible = False
        self.movement = ComposantMouvement(vitesse=9)
        self.combat = ComposantCombat(self)
        self.warping = ComposantWarping(self, fenetre)
        self.interaction = ComposantInteraction(self, fenetre)
       

        transitions = {
            ("idle", "press_move"): "moving",
            ("moving", "release_move"): "idle",
            ("idle", "press_attack"): "attacking",
            ("attacking", "end_attack_anim"): "idle"
        }

        self.fsm = FSM("idle", transitions)
        self.last_moving_direction = "bas"

        # Notifier les observateurs de l'état initial (vie)
        self.notify(self.vie)

    @property
    def state(self):
        return self.fsm.get_state()

    def set_vie(self, nouvelle_vie):
        self.vie = nouvelle_vie
        self.notify(self.vie)  # Notifie les observateurs du changement de vie

    def update_state(self, touches):
        if self.attak != "":
            pass
        else:
            if self.inDialog:
                pass
            else:
                if (touches[pygame.K_LEFT] or touches[pygame.K_RIGHT] or touches[pygame.K_UP] or touches[pygame.K_DOWN]):
                    self.fsm.send_input("press_move")
                else:
                    self.fsm.send_input("release_move")

                if touches[pygame.K_a]:
                    self.fsm.send_input("press_attack")

    def deplacement(self, touches):
        if self.state == "moving":
            largeur, hauteur = self.fenetre.get_size()
            self.rect, self.camerax, self.cameray = self.movement.move(
                self.rect, touches, self.map, largeur, hauteur, self.camerax, self.cameray, self.vie
            )
            self.direction = self.movement.direction
            if self.direction in ["haut", "bas", "gauche", "droite"]:
                self.last_moving_direction = self.direction
        elif self.state == "idle":
            self.direction = "stand_" + self.last_moving_direction

    def attaque(self, touches, ennemiL, map_having_ennemi):
        if self.state == "attacking":
            self.combat.attack(touches, ennemiL, map_having_ennemi)

    def warping(self, objet_dict, Transi):
        self.warping.warp(objet_dict, Transi)

    def read(self, DB):
        self.interaction.read(DB)

    def talk(self, PNG):
        self.interaction.talk(PNG)

    def open(self, COFFRES):
        self.interaction.open(COFFRES)

    def afficher(self):
        if self.attak != "" and self.num_image == len(self.images) - 1:
            self.attak_fin = True
            self.direction = self.attak.replace("hit_", "stand_")
            self.attak = ""
            self.fsm.send_input("end_attack_anim")

        if self.direction == self.old_direction:
            self.timer += 1
            if self.timer > self.delai:
                self.timer = 0
                self.num_image += 1
                if self.num_image >= len(self.images):
                    self.num_image = 0
                self.image = self.images[self.num_image]

            self.fenetre.blit(self.image, (self.rect.x - self.camerax, self.rect.y - self.cameray))
        else:
            self.images = self.dico_images[self.direction]
            self.num_image = 0
            self.old_direction = self.direction
            self.timer += 1
            if self.timer > self.delai:
                self.timer = 0
                self.num_image += 1
                if self.num_image >= len(self.images):
                    self.num_image = 0
                self.image = self.images[self.num_image]

            self.fenetre.blit(self.image, (self.rect.x - self.camerax, self.rect.y - self.cameray))
