#Ici seront faites le modifs pour le perso/ennemi
import pygame
#import random

class elementgraphique:
    def __init__(self,image,fenetre,x=0,y=0):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fenetre = fenetre

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def collide(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

class element_anime(elementgraphique):

    def __init__(self, images, fenetre, x=0, y=0):
        super().__init__(images[0],fenetre, x, y)
        self.images = images
        self.delai = 2
        self.num_image = 0
        self.timer = 0

    def afficher(self):
        self.timer += 1
        if self.timer > self.delai:
            self.timer=0
            self.num_image += 1
            if self.num_image >= len(self.images):
                self.num_image = 0
            self.image=self.images[self.num_image]

        super().afficher()

class element_anime_dir(element_anime):
    def __init__(self, images, fenetre, x=0, y=0):
        self.dico_images = images
        self.direction = "bas"
        self.old_direction = "bas"


        super().__init__(images[self.direction],fenetre, x,y)

    def afficher(self):
        if self.direction == self.old_direction :
            super().afficher()
        else :
            self.images = self.dico_images[self.direction]
            self.num_image = 0
            self.old_direction = self.direction
            super().afficher()




#class du personnage
class perso(element_anime_dir):
    def __init__(self,image,fenetre,x=0,y=0):
        super().__init__(image,fenetre,x,y)
        self.vitesse=3



    def deplacement(self):
        largeur, hauteur = self.fenetre.get_size()
        touches = pygame.key.get_pressed()
        #self.direction="stand"
        if touches[pygame.K_LEFT]:
            self.rect.x-=self.vitesse
            self.direction = "gauche"
        if touches[pygame.K_RIGHT]:
            self.rect.x+=self.vitesse
            self.direction = "droite"
        if touches[pygame.K_UP]:
            self.rect.y-=self.vitesse
            self.direction = "haut"
        if touches[pygame.K_DOWN]:
            self.rect.y+=self.vitesse
            self.direction = "bas"

        #if self.direction=="stand":
            #self.direction=self.old_direction.replace"stand" +"stand"

        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.y<0:
            self.rect.y=0



        if self.rect.y>hauteur-self.rect.h:
            self.rect.y=hauteur-self.rect.h
        elif self.rect.x>largeur-self.rect.w:
            self.rect.x=largeur-self.rect.w

class button(elementgraphique):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)
        self.isClicked = False

    def click(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.isClicked = True

#class des ennemi
class ennemi(elementgraphique):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)
        self.vie=0
        self.spawn=False
        self.use=False
    def vitesse(self):
        self.dx=1
        self.dy=1

    def deplacement(self):
        largeur, hauteur = self.fenetre.get_size()

        self.rect.x+=self.dx
        self.rect.y+=self.dy

        if self.rect.y<0 or self.rect.y> hauteur - self.rect.h:
            self.dy*=-1

        if self.rect.x<0 or self.rect.x> largeur - self.rect.w:
            self.dx*= -1

#def creation_ennemi(x,y):
    #ENNEMI=[]
    #if ROLE=1:
        #ennemi = ennemi(objet["ennemi"],window)
        #ennemi.rect.x = random.randint(ennemi.rect.w,largeur-ennemi.rect.w)
        #ennemi.rect.y = random.randint(ennemi.rect.h,hauteur-ennemi.rect.h)
        #ENNEMI.append(ennemi)

def lecture_objet():
    objet={}


    objet["Lynk"] ={}

    image = pygame.image.load("Source/Lynk/Lynk_stand_gauche.png").convert_alpha()
    objet["Lynk"]["gauche_stand"]=image
    image = pygame.image.load("Source/Lynk/Lynk_stand_droite.png").convert_alpha()
    objet["Lynk"]["droite_stand"]=image
    image = pygame.image.load("Source/Lynk/Lynk_stand_haut.png").convert_alpha()
    objet["Lynk"]["haut_stand"]=image
    image = pygame.image.load("Source/Lynk/Lynk_stand_bas_0.png").convert_alpha()
    objet["Lynk"]["bas_stand"]=image
    objet["Lynk"]["droite"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_droite_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["droite"].append(image)

    objet["Lynk"]["gauche"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_gauche_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["gauche"].append(image)

    objet["Lynk"]["haut"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_haut_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["haut"].append(image)

    objet["Lynk"]["bas"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_walk_bas_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["bas"].append(image)


    objet["Lynk"]["hit_bas"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_hit_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["hit_bas"].append(image)

    objet["Lynk"]["hit_droite"]=[]
    for i in range(9):
      image = pygame.image.load("Source/Lynk/Lynk_hit_droite_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["hit_droite"].append(image)

    objet["Lynk"]["hit_gauche"]=[]
    for i in range(9):
      image = pygame.image.load("Source/Lynk/Lynk_hit_gauche_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["hit_gauche"].append(image)

    objet["Lynk"]["hit_haut"]=[]
    for i in range(9):
      image = pygame.image.load("Source/Lynk/Lynk_hit_haut_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (48, 48))
      objet["Lynk"]["hit_haut"].append(image)



    return objet
