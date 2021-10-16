#Code principal jeu
from constantes import *
from Fonction import *
from menu import *
from Map import *
import pygame
import random
import time
import pygame.mixer
# Initialisation Jeu
pygame.init()

# Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")


objet = lecture_objet()

# Image Personnages
perso = perso(objet["perso_stand_bas"],fenetre)
perso.rect.x = 60
perso.rect.y = 80

# Appel horloge
temps=pygame.time.Clock()

#Définition musique
pygame.mixer.music.load("Source/Musique_&_Son/intro_version_longue.ogg")

i=0
Play=True
Intro,Menu, enJeu = 1,0,0


#Boucle jeu
while Play:

	i+=1
	#print(i)
	temps.tick(30)

	# Lecture clavier
	touches=pygame.key.get_pressed();

	if touches[pygame.K_ESCAPE]: # Échap / Quitter
		Play=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			Play=False
	pass

	###########################
	###########INTRO############
	###########################


	if Intro:
		intro_background.afficher()
		pygame.mixer.music.play()

		if i>=55:
			Intro = 0
			Menu = 1
			pygame.display.flip()
		pygame.display.flip()

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
			pygame.mixer.music.load("Source/Musique_&_Son/Village.ogg")
			pygame.mixer.music.play()
			pygame.display.flip()
		pygame.display.flip()


	############################
	############JEU#############
	############################

	if enJeu:
		#Musique

		#Definition de l'etat
		menu_background.afficher() #Background temporaire pour voir la diff entre menu et enJeu

		perso.afficher(touches)
		perso.deplacement_perso(touches)
		# rafraichissement
		pygame.display.flip()





# Fin programme
pygame.quit()
quit()
