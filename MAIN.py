#Code principal jeu
from Fonction import *
from Map import *
import pygame
import random
import time
from menu import *
from constantes import *
# Initialisation Jeu
pygame.init()

# Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")


objet = lecture_objet()

# lecture de l'image du perso
perso = perso(objet["perso_stand_bas"],fenetre)
perso.rect.x = 60
perso.rect.y = 80

# Appel horloge
temps=pygame.time.Clock()

#Definition de l'etat
Menu, enJeu = 1,0
i=0
Play=True



while Play:

	temps.tick(30)
	print(i)
	i+=1

	# Lecture clavier
	touches=pygame.key.get_pressed();

	if touches[pygame.K_ESCAPE]: # Échap / Quitter
		Play=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			Play=False
	pass


	###########################
	###########MENU############
	###########################


	if Menu:
		menu_background.afficher()
		play_button.afficher()
		play_button.click()

		if play_button.isClicked:
			Menu = 0
			enJeu = 1
			pygame.display.flip()
		pygame.display.flip()


	############################
	############JEU#############
	############################

	if enJeu:
		# rafraichissement
		menu_background.afficher() #Background temporaire pour voir la diff entre menu et enJeu
		perso.afficher(touches)
		perso.deplacement_perso(touches)
		pygame.display.flip()





# Fin programme
pygame.quit()
quit()
