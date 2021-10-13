#Code principal jeu
from TestMap import *
from Fonction import *
import pygame
import random
import time



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
