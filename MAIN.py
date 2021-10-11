#Code principal jeu
import pygame
import random
import time

class elementgraphique:
    def __init__(self,image,fenetre):
        self.image = image
        self.rect = image.get_rect()
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

def lecture_objet():
    objet={}

    image = pygame.image.load("perso.png").convert_alpha()
    objet["perso"]=image

    return objet

#Code principal jeu
#testjjkjk
#modifier par tidiane
# Initialisation Jeu
pygame.init()



# Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")

# Définition fenêtre (à changer si besoin)
largeur=840
hauteur=550
fenetre=pygame.display.set_mode((largeur,hauteur))
objet = lecture_objet()
# lecture de l'image du perso

perso = perso(objet["perso"],fenetre)

# creation d'un rectangle pour positioner l'image du personnage
perso.rect.x = 60
perso.rect.y = 80
# Appel horloge
temps=pygame.time.Clock()

i=0
Play=True
while Play:

	temps.tick(30)
	print(i)
	i+=1




	# Lecture clavier
	touches=pygame.key.get_pressed();

	# rafraichissement
	perso.afficher()

	perso.deplacement_perso(touches)


	pygame.display.flip()
	if touches[pygame.K_ESCAPE]: # Échap / Quitter
		Play=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			Play=False

	pass

# Fin programme
pygame.quit()
quit()