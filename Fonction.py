#Ici seront faites le modifs pour le perso/ennemi
import pygame
#import random

class elementgraphique:
    def __init__(self,image,fenetre):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.fenetre = fenetre

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def collide(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

class element_anime(elementgraphique):

    def __init__(self, images, fen, x, y):
        super().__init__(images[0],fen, x, y)
        self.images = images
        self.delai = 2
        self.num_image = 0
        self.timer = 0

class element_anime_dir(element_anime):
    def __init__(self, images, fen, x, y):
        super().__init__(images[0],fen, x, y)




#class du personnage
class perso(element_anime_dir):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)

    def afficher(self,touches):
        elementgraphique.afficher(self)
        # if touches[pygame.K_RIGHT]:
            #self.image=self(objet["link_r0"],fenetre)
            #self.fenetre.blit(self.image, self.rect)


    def deplacement_perso(self,touches):
        largeur, hauteur = self.fenetre.get_size()
        if touches[pygame.K_LEFT]:
            self.rect.x-=10
        if touches[pygame.K_RIGHT]:
            self.rect.x+=10
        if touches[pygame.K_UP]:
            self.rect.y-=10
        if touches[pygame.K_DOWN]:
            self.rect.y+=10
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

    perso = pygame.image.load("perso.png").convert_alpha()
    objet["perso"]=perso
    perso_walk_gauche=pygame.image.load("Source/Lynk/Lynk_walk_gauche.png").convert_alpha()
    objet["perso_walk_gauche"]=perso_walk_gauche
    perso_walk_droite=pygame.image.load("Source/Lynk/Lynk_walk_droite.png").convert_alpha()
    objet["perso_walk_droite"]=perso_walk_droite
    perso_walk_haut=pygame.image.load("Source/Lynk/Lynk_walk_haut.png").convert_alpha()
    objet["perso_walk_haut"]=perso_walk_haut
    perso_walk_bas=pygame.image.load("Source/Lynk/Lynk_walk.png").convert_alpha()
    objet["perso_walk_bas"]=perso_walk_bas
    perso_stand_gauche=pygame.image.load("Source/Lynk/Lynk_stand_gauche.png").convert_alpha()
    objet["perso_stand_gauche"]=perso_stand_gauche
    perso_stand_droite=pygame.image.load("Source/Lynk/Lynk_stand_droite.png").convert_alpha()
    objet["perso_stand_droite"]=perso_stand_droite
    perso_stand_haut=pygame.image.load("Source/Lynk/Lynk_stand_haut.png").convert_alpha()
    objet["perso_stand_haut"]=perso_stand_haut
    perso_stand_bas=pygame.image.load("Source/Lynk/Lynk_stand_bas.png").convert_alpha()
    objet["perso_stand_bas"]=perso_stand_bas

    #imageBank["Lynk"] ={}
    #imageBank["Lynk"]["droite"]=[]
    #for i in range(4):
      #image = pygame.image.load("Lynk_walk_droite"+str(i)+".png").convert_alpha()
      #image = pygame.transform.scale(image, (48, 48))
      #imageBank["Lynk"]["droite"].append(image)

    #imageBank["Lynk"]["gauche"]=[]
    #for i in range(4):
      #image = pygame.image.load("Lynk_walk_gauche"+str(i)+".png").convert_alpha()
      #image = pygame.transform.scale(image, (48, 48))
      #imageBank["Lynk"]["gauche"].append(image)

    #imageBank["Lynk"]["haut"]=[]
    #for i in range(4):
      #image = pygame.image.load("Lynk_walk_haut"+str(i)+".png").convert_alpha()
      #image = pygame.transform.scale(image, (48, 48))
      #imageBank["Lynk"]["haut"].append(image)

    #imageBank["Lynk"]["bas"]=[]
    #for i in range(4):
      #image = pygame.image.load("Lynk_walk_bas"+str(i)+".png").convert_alpha()
      #image = pygame.transform.scale(image, (48, 48))
      #imageBank["Lynk"]["bas"].append(image)



    return objet
