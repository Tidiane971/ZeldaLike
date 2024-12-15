from Utils.constantes import *
from Utils.loaded_image import *
import pygame.freetype
import pygame

class ElementGraphique:
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
class button(ElementGraphique):
    def __init__(self,image,fenetre):
        ElementGraphique.__init__(self,image,fenetre)
        self.isClicked = False

    #Clic ?
    def click(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.isClicked = True


#Créeation PNJ
class Pnj(ElementGraphique):
    def __init__(self,fenetre,image,x,y, text):
        image = pygame.transform.scale(image, (60,65))
        super().__init__(image,fenetre,x,y)
        self.text = text

    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))

#Creation Coffre
class Coffre(ElementGraphique):
    def __init__(self,fenetre,image,x,y, objet, inclinaison, open):
        image = pygame.transform.scale(image, (60,60))
        super().__init__(image,fenetre,x,y)
        self.inclinaison =inclinaison
        self.open = open
        self.objet = objet


    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))



class DialogBox(ElementGraphique):
    def __init__(self,fenetre,x,y, text,image=pygame.image.load("assets/Source/Map/warp.png").convert_alpha() ):
        super().__init__(image,fenetre,x,y)
        self.text = text


    def afficher(self,perso):
        self.fenetre.blit(self.image, (self.rect.x - perso.camerax, self.rect.y - perso.cameray))


