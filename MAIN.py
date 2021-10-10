import pygame

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



def lecture_objet():
    objet={}

    image = pygame.image.load("perso.png").convert_alpha()
    objet["perso"]=image

    font = pygame.font.Font(None, 34)
    image = font.render('<Escape> pour quitter', True, (255, 255, 255))
    objet["text1"]=image



    return objet

#class concernant le perso
class perso(elementgraphique):
    def __init__(self,image,fenetre):
        elementgraphique.__init__(self,image,fenetre)

    def deplacement_perso(self,touches):
        largeur, hauteur = self.fenetre.get_size()
        if touches[pygame.K_LEFT]:
            self.rect.x-=10*self.sup
        if touches[pygame.K_RIGHT]:
            self.rect.x+=10*self.sup
        if touches[pygame.K_UP]:
            self.rect.y-=10*self.sup
        if touches[pygame.K_DOWN]:
            self.rect.y+=10*self.sup
        if self.rect.x<0:
            self.rect.x=0*self.sup
        elif self.rect.y<0:
            self.rect.y=0*self.sup

        if self.rect.y>hauteur-self.rect.h:
            self.rect.y=hauteur-self.rect.h
        elif self.rect.x>largeur-self.rect.w:
            self.rect.x=largeur-self.rect.w

# Initialisation de la bibliotheque pygame
pygame.init()


#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))




perso = perso(objet["perso"],fenetre)

# creation d'un rectangle pour positioner l'image du personnage
perso.rect.x = 60
perso.rect.y = 80


# lecture de l'image du fond

fond = elementgraphique(objet["fond"],fenetre)


# Creation de l'image correspondant au texte

text1= elementgraphique(objet["text1"],fenetre)



# creation d'un rectangle pour positioner l'image du texte
text1.rect.x = 10
text1.rect.y = 10


# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()




i=1;
continuer=True
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    print (i)



    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=False

    # Affichage du fond


    fond.afficher()

    # Affichage et déplacement du perso
    perso.afficher()
    perso.deplacement_perso(touches)

    text1.afficher()
    font = pygame.font.Font(None, 34)


    # rafraichissement
    pygame.display.flip()


    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = False	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
