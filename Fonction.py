#Importation Fichier
from constantes import *

#Importation module
import pygame.freetype
import keyboard
import pygame
#import random
import copy
import time

#Créeation image
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


#Espace cliquable
class button(elementgraphique):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)
        self.isClicked = False

    #Clic ?
    def click(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.isClicked = True


#Créeation PNJ
class pnj(elementgraphique):
    def __init__(self,fenetre,image,x,y, text, inclinaison):
        image = pygame.transform.scale(image, (70,70))
        super().__init__(image,fenetre,x,y)
        self.text = text

    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))

#Creation Coffre
class coffre(elementgraphique):
    def __init__(self,fenetre,image,x,y, objet, inclinaison, open):
        image = pygame.transform.scale(image, (60,60))
        super().__init__(image,fenetre,x,y)
        self.inclinaison =inclinaison
        self.open = open
        self.objet = objet


    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))



class DialogBox(elementgraphique):
    def __init__(self,fenetre,x,y, text,image=pygame.image.load("Source/Map/warp.png").convert_alpha() ):
        super().__init__(image,fenetre,x,y)
        self.text = text


    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))


# Objet inGame
class Objet():
    def __init__(self,image,nom,type):
        self.image = image
        self.nom = nom
        self.type = type



#MAP / ChangementMap
class Map(elementgraphique):
    def __init__(self,image,fenetre,x=0,y=0):
        super().__init__(image,fenetre,x,y)

    def afficher(self, camerax, cameray):
        self.fenetre.blit(self.image, (self.rect.x-camerax, self.rect.y -cameray))

# class Warp(elementgraphique):
#     def __init__(self,fenetre,x,y, inclinaison, destination, lock,image=pygame.image.load("Source/Map/warp.png").convert_alpha() ):
#         super().__init__(image,fenetre,x,y)
#         self.inclinaison = inclinaison
#         self.destination = destination
#         self.lock = lock


#Gestion inventaire
class Inventaire(elementgraphique):
    def __init__(self,fenetre,perso):
        self.perso = perso
        self.x = 450
        self.y = 90
        #self.cursor = pygame.image.load("Source/Autre/cursor/select.png").convert_alpha()
        #self.image = pygame.transform.scale(image, (25, 25))
        self.image = pygame.image.load("Source/Lynk/Inventaire/INVENTAIRE.png")
        super().__init__(self.image,fenetre,self.x,self.y)
        self.contenu = []
        self.open = False
        self.slot = {
        "slot1" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 469, y = 319),
        "slot2" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 529, y = 319),
        "slot3" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 582, y = 319),
        "slot4" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 638, y = 319),
        "slot5" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 694, y = 319),

        "slot6" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 469, y = 370),
        "slot7" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 525, y = 370),
        "slot8" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 582, y = 370),
        "slot9" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 636, y = 370),
        "slot10" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x =694, y = 370),

        "slot11" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 469, y = 421),
        "slot12" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 525, y = 421),
        "slot13" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 582, y = 421),
        "slot14" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 638, y = 421),
        "slot15" : elementgraphique( fenetre = self.fenetre ,image = pygame.image.load("Source/Map/slot.png") , x = 694, y = 421),
        }

    def afficher(self):
        if keyboard.is_pressed("e") and not self.open:
            self.open = True
            self.perso.inDialog = True
            pygame.time.delay(120)
        elif keyboard.is_pressed("e") and self.open:
            self.open = False
            pygame.time.delay(120)
            self.perso.inDialog = False

        if self.open:
            self.fenetre.blit(self.image, (self.rect.x , self.rect.y))
            for k in range(len(self.contenu)):
                self.contenu[k].image.rect.x = self.slot["slot"+str(k+1)].rect.x
                self.contenu[k].image.rect.y = self.slot["slot"+str(k+1)].rect.y
                self.contenu[k].image.afficher()

    def consume(self, perso,pos):

        if perso.vie <16:
            if self.open:
                for slot, valeur in self.slot.items():
                    if(valeur.rect.collidepoint(pos)):
                        if(len(self.contenu)>0):
                            if(self.contenu[int(slot[4:])-1].nom == "Une Potion de Heal" ):
                                perso.vie +=2
                                self.contenu.pop(int(slot[4:])-1)








#Element animé
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


#Direction d'animation
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
    def __init__(self,image,fenetre,camerax,cameray,map,map_id,x=0,y=0 ):
        super().__init__(image,fenetre,x,y)
        self.vie=16
        self.vitesse=9
        self.attak_fin=True
        self.attak=""
        self.camerax = camerax
        self.cameray = cameray
        self.map = map
        self.map_id = map_id
        self.fenetre = fenetre
        self.inDialog = False
        self.pressed = False
        self.inventaire = Inventaire(fenetre = self.fenetre, perso = self )
        self.invincible = False


    #Affichage Perso
    def afficher(self):
        if self.attak!="" and self.num_image==len(self.images)-1:
            self.attak_fin=True
            self.direction=self.attak.replace("hit_", "stand_")
            self.attak=""


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


    #Mort perso
    #def dead(self, vie):
        #if self.vie==0:
            #self.direction="dead"
        #super().afficher()

    #Déplacement Perso/Focus
#<<<<<<< Updated upstream
    #def deplacement(self):
#=======
    def deplacement(self, vie):
#>>>>>>> Stashed changes
        largeur, hauteur = self.fenetre.get_size()
        rect_provisoire = copy.copy(self.rect)
        cameraxprovisoire = self.camerax

        #Lecture Flèches
        touches = pygame.key.get_pressed()
        if self.vie!=0 and touches[pygame.K_LEFT]:
            self.delai = 1 #Vitesse animation
            self.direction="gauche" #Direction perso
            rect_provisoire.x-=self.vitesse #Déplacement Focus
        elif self.vie!=0 and self.direction=="gauche":
            self.direction="stand_gauche"
            self.delai=3

        if self.vie!=0 and touches[pygame.K_RIGHT]:
            self.delai = 1 #Vitesse animation
            self.direction="droite" #Direction perso
            rect_provisoire.x+=self.vitesse #Déplacement Focus

        elif self.vie!=0 and self.direction=="droite":
            self.direction="stand_droite"
            self.delai=3

        if self.vie!=0 and touches[pygame.K_UP]:
            self.delai = 1.5 #Vitesse animation
            self.direction="haut" #Direction perso
            rect_provisoire.y-=self.vitesse #Déplacement Focus
        elif self.vie!=0 and self.direction=="haut":
            self.direction="stand_haut"
            self.delai=3

        if self.vie!=0 and touches[pygame.K_DOWN]:
            self.delai = 1.5 #Vitesse animation
            self.direction="bas" #Direction perso
            rect_provisoire.y+=self.vitesse #Déplacement Focus
        elif self.vie!=0 and self.direction=="bas":
            self.direction="stand_bas"
            self.delai=3

        if(self.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==0 and
           self.map[2][rect_provisoire.y//64][(rect_provisoire.x+52)//64]==0 and
           self.map[2][(rect_provisoire.y+52)//64][rect_provisoire.x//64]==0 and
           self.map[2][(rect_provisoire.y+52)//64][(rect_provisoire.x+52)//64]==0):

            self.rect = rect_provisoire

            self.camerax = self.rect.x-(largeur//2)
            self.cameray = self.rect.y-(hauteur//2)

        #else:
            #print("BLOQUER")


        #Perso attaque
        if touches[pygame.K_a] and self.direction=="stand_bas":
            self.delai=1
            self.attak="hit_bas"
            self.direction="hit_bas"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_haut":
            self.delai=1
            self.attak="hit_haut"
            self.direction="hit_haut"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_gauche":
            self.delai=1
            self.attak="hit_gauche"
            self.direction="hit_gauche"
            self.attak_fin=False

        if touches[pygame.K_a] and self.direction=="stand_droite":
            self.delai=1
            self.attak="hit_droite"
            self.direction="hit_droite"
            self.attak_fin=False

        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.y<0:
            self.rect.y=0


        limitex,limitey= self.map[3]
        if self.cameray< 0:
            self.cameray =0
        if self.camerax < 0:
            self.camerax =0
        if self.camerax > limitex-largeur:
            self.camerax = limitex - largeur
        if self.cameray > limitey-hauteur:
            self.cameray = limitey - hauteur

#---------------------------------------------DIALOGUE---------------------------------------------------#
#UTILISE LE MODULE KEYBOARD @Tidiane



    def warping(self, objet_dict):
        rect_provisoire = copy.copy(self.rect)
        warp_case = 0
        if(self.direction == "haut"):
            warp_case = self.map[2][(rect_provisoire.y-64+52)//64][(rect_provisoire.x)//64]
            rect_provisoire.y-=64
        if(self.direction == "droite"):
            warp_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x+64)//64]
            rect_provisoire.x+=64
        if(self.direction == "bas"):
            warp_case = self.map[2][(rect_provisoire.y+64)//64][(rect_provisoire.x)//64]
            rect_provisoire.y+=64
        if(self.direction == "gauche"):
            warp_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x-64)//64]
            rect_provisoire.x-=64


        if int(str(warp_case)[0]) == 2:

            if(len(str(warp_case))<8):
                for fondu in Transi:
                    self.fenetre.blit(fondu, (0,0))
                    pygame.display.flip()
                    time.sleep(0.05)

                self.map_id = int(str(warp_case)[1])
                self.rect.x = int(str(warp_case)[2:4])*64
                self.rect.y = int(str(warp_case)[4:6])*64
                inclinaison = int(str(warp_case)[6])



                if(inclinaison==1):
                    self.rect.y -= 64
                if(inclinaison==2):
                    self.rect.x += 64
                if(inclinaison==3):
                    self.rect.y += 64
                if(inclinaison==4):
                    self.rect.x -= 64

                self.camerax = self.rect.x-(largeur//2)
                self.cameray = self.rect.y-(hauteur//2)
            else:

                if(objet_dict["Clé1"] in self.inventaire.contenu and objet_dict["Clé2"] in self.inventaire.contenu and objet_dict["Clé3"] in self.inventaire.contenu ):
                    for fondu in Transi:
                        self.fenetre.blit(fondu, (0,0))
                        pygame.display.flip()
                        time.sleep(0.05)

                    self.map_id = int(str(warp_case)[1])
                    self.rect.x = int(str(warp_case)[2:4])*64
                    self.rect.y = int(str(warp_case)[4:6])*64
                    inclinaison = int(str(warp_case)[6])



                    if(inclinaison==1):
                        self.rect.y -= 64
                    if(inclinaison==2):
                        self.rect.x += 64
                    if(inclinaison==3):
                        self.rect.y += 64
                    if(inclinaison==4):
                        self.rect.x -= 64

                    self.camerax = self.rect.x-(largeur//2)
                    self.cameray = self.rect.y-(hauteur//2)





    #Chat PNJ
    def read(self, DB):
        rectBox = (80,400)
        boxImage = pygame.image.load("Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715,144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.rect)

        if(touches[pygame.K_s]):
            if not self.pressed:
                self.pressed = True
        if(touches[pygame.K_q]):
            if self.inDialog:
                self.pressed = False
                self.inDialog = False

        if self.pressed:
            if(self.direction == "stand_haut"):
                if self.map[2][(rect_provisoire.y-64)//64][(rect_provisoire.x)//64]==3:
                    self.inDialog = True
                    rect_provisoire.y-=64
                    for dialog in DB:
                        for d in dialog:
                            if(rect_provisoire.colliderect(d.rect)):
                                self.fenetre.blit(boxImage, rectBox)
                                myfont.render_to(self.fenetre, (152,452), d.text[0], (0,0,0))
                                if len(d.text)>1:
                                    myfont.render_to(self.fenetre, (152,460), d.text[1], (0,0,0))
                                if len(d.text)>2:
                                    myfont.render_to(self.fenetre, (152,490), d.text[2], (0,0,0))


    def talk(self,PNG):

        rectBox = (80,400)
        boxImage = pygame.image.load("Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715,144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.rect)

        if(touches[pygame.K_s]):
            if not self.pressed:
                self.pressed = True
        if(touches[pygame.K_q]):
            if self.inDialog:
                self.pressed = False
                self.inDialog = False




        if self.pressed:
            pnj_case = 0
            if(self.direction == "stand_haut"):
                if(self.map_id==3):
                    pnj_case = self.map[2][(rect_provisoire.y-128)//64][(rect_provisoire.x)//64]
                    rect_provisoire.y-=128
                else:
                    pnj_case = self.map[2][(rect_provisoire.y-64)//64][(rect_provisoire.x)//64]
                    rect_provisoire.y-=64

            if(self.direction == "stand_droite"):
                pnj_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x+64)//64]
                rect_provisoire.x+=64
            if(self.direction == "stand_bas"):
                pnj_case = self.map[2][(rect_provisoire.y+64)//64][(rect_provisoire.x)//64]
                rect_provisoire.y+=64
            if(self.direction == "stand_gauche"):
                pnj_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x-64)//64]
                rect_provisoire.x-=64


            if pnj_case==4:
                self.inDialog = True

                for pnj in PNG:
                    for p in pnj:
                        if(rect_provisoire.colliderect(p.rect)):
                            self.fenetre.blit(boxImage, rectBox)
                            myfont.render_to(self.fenetre, (152,432), p.text[0], (0,0,0))
                            if len(p.text)>1:
                                myfont.render_to(self.fenetre, (152,462), p.text[1], (0,0,0))
                            if len(p.text)>2:

                                myfont.render_to(self.fenetre, (152,492), p.text[2], (0,0,0))


    def open(self,COFFRES):

        rectBox = (80,400)
        boxImage = pygame.image.load("Source/Autre/dialog_box.png")
        boxImage = pygame.transform.scale(boxImage, (715,144))
        touches = pygame.key.get_pressed()
        rect_provisoire = copy.copy(self.rect)

        if(touches[pygame.K_s]):
            if not self.pressed:
                self.pressed = True
        if(touches[pygame.K_q]):
            if self.inDialog:
                self.pressed = False
                self.inDialog = False


        if self.pressed:
            pnj_case = 0
            if(self.direction == "stand_haut"):
                pnj_case = self.map[2][(rect_provisoire.y-64)//64][(rect_provisoire.x)//64]
                rect_provisoire.y-=64
            if(self.direction == "stand_droite"):
                pnj_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x+64)//64]
                rect_provisoire.x+=64
            if(self.direction == "stand_bas"):
                pnj_case = self.map[2][(rect_provisoire.y+64)//64][(rect_provisoire.x)//64]
                rect_provisoire.y+=64
            if(self.direction == "stand_gauche"):
                rect_provisoire.x-=64
                pnj_case = self.map[2][(rect_provisoire.y)//64][(rect_provisoire.x-64)//64]


            if pnj_case==5:
                for coffre in COFFRES:
                    for c in coffre:
                        if c.open == False:
                            if(rect_provisoire.colliderect(c.rect)):
                                if not c.open:

                                    self.fenetre.blit(boxImage, rectBox)
                                    myfont.render_to(self.fenetre, (152,452),"Vous avez trouvé " + c.objet.nom+ " !", (0,0,0))

                                    if c.inclinaison ==3:
                                        c.image = pygame.image.load("Source/Autre/Chest/chest_open_bas.png")
                                        c.image = pygame.transform.scale(c.image, (60,60))


                                        if touches[pygame.K_q]:
                                            self.inventaire.contenu.append(c.objet)
                                            c.open = True


#-----------------------------------------------------ENNEMI------------------------------------------------------#

class ennemi(element_anime_dir):
    def __init__(self,image,fenetre,perso,x,y, dir):
        super().__init__(image,fenetre,x,y)
        self.vie=16
        self.vitesse=9
        self.attak_fin=True
        self.attak=""
        self.fenetre = fenetre
        self.inDialog = False
        self.pressed = False
        self.perso =perso
        self.map = map
        self.dir = dir








    #Affichage
    def afficher(self,perso):


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


        rect_provisoire = copy.copy(self.rect)



        #Lecture Flèches
        touches = pygame.key.get_pressed()
        if self.dir == "gauche" :
            self.delai = 1 #Vitesse animation
            self.direction="gauche" #Direction perso
            rect_provisoire.x-=self.vitesse

        if self.dir == "droite":
            self.delai = 1 #Vitesse animation
            self.direction="droite" #Direction perso
            rect_provisoire.x+=self.vitesse #Déplacement Focus

        if self.dir == "haut":
            self.delai = 1.5 #Vitesse animation
            self.direction="haut" #Direction perso
            rect_provisoire.y-=self.vitesse #Déplacement Focus


        if self.dir == "bas":
            self.delai = 1.5 #Vitesse animation
            self.direction="bas" #Direction perso
            rect_provisoire.y+=self.vitesse #Déplacement Focus




        if(perso.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==0 or perso.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==6):
            (perso.map[2])[self.rect.y//64][self.rect.x//64] = 0
            self.rect = rect_provisoire
            (perso.map[2])[rect_provisoire.y//64][rect_provisoire.x//64] = 6




        elif(perso.map[2][rect_provisoire.y//64][rect_provisoire.x//64]==1):
            if(self.dir == "gauche"):

                self.dir = "droite"

            elif(self.dir == "droite"):
                self.dir = "gauche"

            elif(self.dir == "haut"):
                self.dir = "bas"

            elif(self.dir == "bas"):
                self.dir = "haut"

    def attaque(self, perso):
        if(self.rect.colliderect(perso.rect) and not perso.invincible):
            perso.vie-=1
            global a
            a = pygame.time.get_ticks()
            perso.invincible = True


        if(perso.invincible):
            perso.image = pygame.image.load("Source/Map/warp.png")
            if( pygame.time.get_ticks() - a > 2500):
                perso.invincible=False










#Dictionnaire Images
def lecture_objet():
    objet={}

    #curseur
    image=pygame.image.load("Source/Autre/cursor/select.png").convert_alpha()
    image = pygame.transform.scale(image, (25, 25))
    objet["select"]=image

    #coeur
    image=pygame.image.load("Source/Lynk/heart/heart_0.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["heart_0"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_1.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["heart_1"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_2.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["heart_2"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_3.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["heart_3"]=image
    image=pygame.image.load("Source/Lynk/heart/heart_4.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["heart_4"]=image

    #coeur à ramasser
    image=pygame.image.load("Source/Lynk/heart_object/life_object_0.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["vie_0"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_1.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["vie_1"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_2.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["vie_2"]=image
    image=pygame.image.load("Source/Lynk/heart_object/life_object_3.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 52))
    objet["vie_3"]=image


    #animation Lynk
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
    for i in range(8):
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

    #image ennemie
    objet["ennemi"]={}
    objet["ennemi"]["korogu"]={}
    objet["ennemi"]["korogu"]["bas"]=[]
    for i in range(4):
        image = pygame.image.load("Source/Enemy/korogu/korogu_walk_bas_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (52, 52))
        objet["ennemi"]["korogu"]["bas"].append(image)

    objet["ennemi"]["korogu"]["haut"]=[]
    for i in range(4):
        image = pygame.image.load("Source/Enemy/korogu/korogu_walk_haut_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (52, 52))
        objet["ennemi"]["korogu"]["haut"].append(image)

    objet["ennemi"]["korogu"]["droite"]=[]
    for i in range(4):
        image = pygame.image.load("Source/Enemy/korogu/korogu_walk_droite_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (52, 52))
        objet["ennemi"]["korogu"]["droite"].append(image)

    objet["ennemi"]["korogu"]["gauche"]=[]
    for i in range(4):
        image = pygame.image.load("Source/Enemy/korogu/korogu_walk_gauche_"+str(i)+".png").convert_alpha()
        image = pygame.transform.scale(image, (52, 52))
        objet["ennemi"]["korogu"]["gauche"].append(image)

    objet["ennemi"]["boss"]={}
    objet["ennemi"]["boss"]["bas"]=[]

    image = pygame.image.load("Source/PNJ/Boss/boss_all.png").convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    objet["ennemi"]["boss"]["bas"].append(image)

    objet["ennemi"]["boss"]["haut"]=[]

    image = pygame.image.load("Source/PNJ/Boss/boss_all.png").convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    objet["ennemi"]["boss"]["haut"].append(image)

    objet["ennemi"]["boss"]["droite"]=[]

    image = pygame.image.load("Source/PNJ/Boss/boss_all.png").convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    objet["ennemi"]["boss"]["droite"].append(image)

    objet["ennemi"]["boss"]["gauche"]=[]

    image = pygame.image.load("Source/PNJ/Boss/boss_all.png").convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    objet["ennemi"]["boss"]["gauche"].append(image)




    return objet


def fill(surface, color):
    w, h = surface.get_size()
    r,g,b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x,y))[3]
            surface.set_at((x,y), pygame.Color(r,g,b,a))
