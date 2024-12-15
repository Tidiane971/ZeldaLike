from Graphique.animation import element_anime_dir
import pygame
import copy
from patterns import Subject  

class EnemyType:
    def __init__(self, images, vie, vitesse):
        self.images = images
        self.vie = vie
        self.vitesse = vitesse

class Ennemi(element_anime_dir, Subject):
    def __init__(self, enemy_type, fenetre, x, y, direction="gauche"):
        element_anime_dir.__init__(self, enemy_type.images, fenetre, x, y)
        Subject.__init__(self)  # Initialiser le Subject
        self.vie = enemy_type.vie
        self.vitesse = enemy_type.vitesse
        self.attak_fin = True
        self.attak = ""
        self.fenetre = fenetre
        self.inDialog = False
        self.pressed = False
        self.invincible = False
        self.dir = direction
        self.map = None

        self.state = "patrol" 
        self.transitions = {
            ("idle", "see_player"): "chase",
            ("patrol", "see_player"): "chase",
            ("chase", "lose_player"): "patrol",
            ("chase", "player_close"): "attack",
            ("attack", "player_far"): "chase"
        }

        # Notifier l'état initial (vie)
        self.notify(self.vie)

    def set_map(self, map_data):
        self.map = map_data

    def set_vie(self, nouvelle_vie):
        self.vie = nouvelle_vie
        self.notify(self.vie)  # On notifie que la vie a changé

    def send_input(self, input_symbol):
        if (self.state, input_symbol) in self.transitions:
            self.state = self.transitions[(self.state, input_symbol)]

    def update_behavior(self, perso):
        dist_x = abs(perso.rect.x - self.rect.x)
        dist_y = abs(perso.rect.y - self.rect.y)
        distance = (dist_x**2 + dist_y**2)**0.5

        if distance < 200 and self.state in ["idle", "patrol"]:
            self.send_input("see_player")
        if self.state == "chase" and distance > 300:
            self.send_input("lose_player")
        if self.state == "chase" and distance < 64:
            self.send_input("player_close")
        if self.state == "attack" and distance > 128:
            self.send_input("player_far")

    def afficher(self, perso):
        # Code existant inchangé
        if self.direction == self.old_direction :
            self.timer += 1
            if self.timer > self.delai:
                self.timer=0
                self.num_image += 1
                if self.num_image >= len(self.images):
                    self.num_image = 0
                self.image=self.images[self.num_image]

            self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))
        else :
            self.images = self.dico_images[self.direction]
            self.num_image = 0
            self.old_direction = self.direction
            self.timer += 1
            if self.timer > self.delai:
                self.timer=0
                self.num_image += 1
                if self.num_image >= len(self.images):
                    self.num_image = 0
                self.image=self.images[self.num_image]

            self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y-perso.cameray))

    def deplacement(self, perso):
        self.update_behavior(perso)
        if self.state == "patrol":
            self.deplacement_patrol(perso)
        elif self.state == "chase":
            self.deplacement_chase(perso)
        elif self.state == "attack":
            pass

    def deplacement_patrol(self, perso):
        rect_provisoire = copy.copy(self.rect)
        if self.dir == "gauche":
            self.delai = 1
            self.direction="gauche"
            rect_provisoire.x-=self.vitesse
        elif self.dir == "droite":
            self.delai = 1
            self.direction="droite"
            rect_provisoire.x+=self.vitesse
        elif self.dir == "haut":
            self.delai = 1.5
            self.direction="haut"
            rect_provisoire.y-=self.vitesse
        elif self.dir == "bas":
            self.delai = 1.5
            self.direction="bas"
            rect_provisoire.y+=self.vitesse

        if ((self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==0) or 
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==6):
            self.map[2][self.rect.y//64][self.rect.x//64] = 0
            self.rect = rect_provisoire
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64] = 6
        else:
            if self.dir == "gauche":
                self.dir = "droite"
            elif self.dir == "droite":
                self.dir = "gauche"
            elif self.dir == "haut":
                self.dir = "bas"
            elif self.dir == "bas":
                self.dir = "haut"

    def deplacement_chase(self, perso):
        rect_provisoire = copy.copy(self.rect)
        dx = perso.rect.x - self.rect.x
        dy = perso.rect.y - self.rect.y

        speed = 4
        if dx > 0:
            rect_provisoire.x += speed
            self.direction = "droite"
        elif dx < 0:
            rect_provisoire.x -= speed
            self.direction = "gauche"

        if dy > 0:
            rect_provisoire.y += speed
            self.direction = "bas"
        elif dy < 0:
            rect_provisoire.y -= speed
            self.direction = "haut"

        if ((self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==0) or 
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==6):
            self.map[2][self.rect.y//64][self.rect.x//64] = 0
            self.rect = rect_provisoire
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64] = 6

    def deplacementBoss(self, perso):
        rect_provisoire = copy.copy(self.rect)
        dx = perso.rect.x - self.rect.x
        dy = perso.rect.y - self.rect.y
        speed = 4

        if dx > 0:
            rect_provisoire.x += speed
            self.direction = "droite"
        elif dx < 0:
            rect_provisoire.x -= speed
            self.direction = "gauche"

        if dy > 0:
            rect_provisoire.y += speed
            self.direction = "bas"
        elif dy < 0:
            rect_provisoire.y -= speed
            self.direction = "haut"

        if self.invincible or perso.vie %4 ==0:
            rect_provisoire.x -= 5
            rect_provisoire.y -= 5

        if ((self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==0) or 
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==6):
            self.map[2][self.rect.y//64][self.rect.x//64] = 0
            self.rect = rect_provisoire
            self.map[2][rect_provisoire.y//64][rect_provisoire.x//64] = 6

    def attaque(self, perso):
        if(self.rect.colliderect(perso.rect) and not perso.invincible and not self.invincible):
            perso.vie-=1
            global a
            a = pygame.time.get_ticks()
            perso.invincible = True

        if(perso.invincible):
            perso.image = pygame.image.load("assets/Source/Map/warp.png")
            if( pygame.time.get_ticks() - a > 2500):
                perso.invincible=False
