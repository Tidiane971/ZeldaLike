#Ici seront faites le modifs pour le perso/ennemi
import pygame
import mapgrid
#import random
import Map
import copy
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
    def __init__(self,image,fenetre,camerax,cameray,x=0,y=0):
        super().__init__(image,fenetre,x,y)
        self.vie=12
        self.vitesse=5.5
        self.attak_fin=True
        self.attak=""
        self.camerax = camerax
        self.cameray = cameray



    def afficher(self):
        if self.attak!="" and self.num_image==len(self.images)-1:
            self.attak_fin=True
            self.direction=self.attak.replace("hit_", "stand_")
            self.attak=""
            print("fin attaque")
            print(self.direction)

        if self.direction == self.old_direction :
            self.timer += 1
            if self.timer > self.delai:
                self.timer=0
                self.num_image += 1
                if self.num_image >= len(self.images):
                    self.num_image = 0
                self.image=self.images[self.num_image]

            self.fenetre.blit(self.image, (self.rect.x-self.camerax, self.rect.y-self.cameray))
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

            self.fenetre.blit(self.image, (self.rect.x-self.camerax, self.rect.y-self.cameray))




    def deplacement(self):
        largeur, hauteur = self.fenetre.get_size()
        touches = pygame.key.get_pressed()

        rect_provisoire = copy.copy(self.rect)
        cameraxprovisoire = self.camerax
        

        if touches[pygame.K_LEFT]:
            self.delai = 1

            rect_provisoire.x-=self.vitesse


            self.direction = "gauche"
        elif self.direction=="gauche":
            self.direction="stand_gauche"

        if touches[pygame.K_RIGHT]:
            self.delai = 1

            rect_provisoire.x+=5.5
            cameraxprovisoire+=self.vitesse

            self.direction = "droite"
        elif self.direction=="droite":
            self.direction="stand_droite"

        if touches[pygame.K_UP]:
            self.delai = 2
            rect_provisoire.y-=self.vitesse

            self.direction = "haut"
        elif self.direction=="haut":
            self.direction="stand_haut"

        if touches[pygame.K_DOWN]:
            self.delai = 2
            rect_provisoire.y+=self.vitesse

            self.direction = "bas"
        elif self.direction=="bas":
            self.direction="stand_bas"

        if(mapgrid.T[rect_provisoire.y//64][rect_provisoire.x//64]==0 and
           mapgrid.T[rect_provisoire.y//64][(rect_provisoire.x+62)//64]==0 and
           mapgrid.T[(rect_provisoire.y+62)//64][rect_provisoire.x//64]==0 and
           mapgrid.T[(rect_provisoire.y+62)//64][(rect_provisoire.x+62)//64]==0):

            self.rect = rect_provisoire

            self.camerax = self.rect.x-(largeur//2)
            self.cameray = self.rect.y-(hauteur//2)
        else:
            print("BLOQUER")




        if touches[pygame.K_a] and self.direction=="stand_bas":
            self.attak="hit_bas"
            self.direction="hit_bas"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_haut":
            self.attak="hit_haut"
            self.direction="hit_haut"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_gauche":
            self.attak="hit_gauche"
            self.direction="hit_gauche"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_droite":
            self.attak="hit_droite"
            self.direction="hit_droite"
            self.attak_fin=False

        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.y<0:
            self.rect.y=0




#Fonction bouton graphique
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
        self.vie=3
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
        #ennemi = ennemi(objet["ennemi"][random.randint("sauteur","octorok")],window)
        #ennemi.rect.x = random.randint(ennemi.rect.w,largeur-ennemi.rect.w)
        #ennemi.rect.y = random.randint(ennemi.rect.h,hauteur-ennemi.rect.h)
        #ENNEMI.append(ennemi)


#Lecture du dictinnaire des images
def lecture_objet():
    objet={}

    #image ennemie
    #objet["ennemi"]={}
    #objet["ennemi"]["octorok"]={}
    #objet["ennemi"]["octorok"]["stand_bas"]=[]
    #for i in range():

    #objet["ennemi"]["sauteur"]={}
    #objet["ennemi"]["sauteur"]["stand_bas"]=[]
    #for i in range():


    #coeur
    image=pygame.image.load("Source/Lynk/heart/heart_0.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["heart_0"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_1.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["heart_1"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_2.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["heart_2"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_3.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["heart_3"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_4.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["heart_4"]=image

    #coeur à ramasser
    image=pygame.image.load("Source/Lynk/heart_object/life_object_0.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["vie_0"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_1.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["vie_1"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_2.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["vie_2"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_3.png").convert_alpha()
    image = pygame.transform.scale(image, (62, 62))
    objet["vie_3"]=image

    #animation debout
    #vers le bas
    objet["Lynk"]={}

    objet["Lynk"]["stand_bas"]=[]
    for i in range(4):
        image=pygame.image.load("Source/Lynk/Lynk_stand_bas_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (62, 62))
        objet["Lynk"]["stand_bas"].append(image)

    #vers la droite
        objet["Lynk"]["stand_droite"]=[]
        for i in range(4):
            image=pygame.image.load("Source/Lynk/Lynk_stand_droite_"+str(i)+".png").convert_alpha()
            image = pygame.transform.scale(image, (62, 62))
            objet["Lynk"]["stand_droite"].append(image)

    #vers la gauche
        objet["Lynk"]["stand_gauche"]=[]
        for i in range(4):
            image=pygame.image.load("Source/Lynk/Lynk_stand_gauche_"+str(i)+".png").convert_alpha()
            image = pygame.transform.scale(image, (62, 62))
            objet["Lynk"]["stand_gauche"].append(image)

    #vers la haut
        objet["Lynk"]["stand_haut"]=[]
        for i in range(4):
            image=pygame.image.load("Source/Lynk/Lynk_stand_haut_"+str(i)+".png").convert_alpha()
            image = pygame.transform.scale(image, (62, 62))
            objet["Lynk"]["stand_haut"].append(image)

    #animation marche droite
    objet["Lynk"]["droite"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_droite_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["droite"].append(image)

    #animation marche gauche
    objet["Lynk"]["gauche"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_gauche_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["gauche"].append(image)

    #animation marche haut
    objet["Lynk"]["haut"]=[]
    for i in range(10):
      image = pygame.image.load("Source/Lynk/Lynk_walk_haut_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["haut"].append(image)

    #animation marche bas
    objet["Lynk"]["bas"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_walk_bas_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["bas"].append(image)

    #animation attaque épée
    objet["Lynk"]["hit_bas"]=[]
    for i in range(6):
      image = pygame.image.load("Source/Lynk/Lynk_hit_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["hit_bas"].append(image)

    #animation attaque épée droite
    objet["Lynk"]["hit_droite"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_hit_droite_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["hit_droite"].append(image)

    #animation attaque épée gauche
    objet["Lynk"]["hit_gauche"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_hit_gauche_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["hit_gauche"].append(image)

    #animation attaque épée haut
    objet["Lynk"]["hit_haut"]=[]
    for i in range(8):
      image = pygame.image.load("Source/Lynk/Lynk_hit_haut_"+str(i)+".png").convert_alpha()
      image = pygame.transform.scale(image, (62, 62))
      objet["Lynk"]["hit_haut"].append(image)

    #animation mort
    objet["Lynk"]["dead"]=[]
    for i in range(4):
        image = pygame.image.load("Source/Lynk/Lynk_dead_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (62, 62))
        objet["Lynk"]["dead"].append(image)

    return objet
