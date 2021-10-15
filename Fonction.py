#Ici seront faites le modifs pour le perso/ennemi
import pygame

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



class perso(elementgraphique):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)


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


def lecture_objet():
    objet={}

    perso = pygame.image.load("perso.png").convert_alpha()
    objet["perso"]=perso

    return objet
