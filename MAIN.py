from constantes import *
from Fonction import *
from menu import *
from Map import *
from Warp import *
#from Film import *
import pygame
import random
import time
import pygame.mixer
import mapgrid
#Code principal jeu
# Initialisation Jeu
pygame.init()

# Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")


#---Lectures des images
objet = lecture_objet()

# Image Lynk
perso = perso(objet["Lynk"],fenetre,x=largeur//2+120,y=hauteur//2,camerax=CameraX,cameray=CameraY,map = actual_map, map_id = 0 )

#Image coeurs
v=0
tab_vie=[]
for i in range(4):
	vie= elementgraphique(objet["heart_"+str(v)],fenetre,x=10+30*i,y=10)
	tab_vie.append(vie)

# Appel horloge
temps=pygame.time.Clock()

#Définition musique
pygame.mixer.music.load("Source/Musique_&_Son/intro_theme1.ogg")

#Variable utiles
i=0
Play=True
Intro, Menu, enJeu, GameOver = 1,0,0,0

x=0


#Boucle jeu
while Play:

	i+=1
	#print(i)
	temps.tick(30)

	# Lecture clavier
	touches=pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE]: # Échap / Quitter
		Play=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			Play=False

	###########################
	###########INTRO############
	###########################

	if Intro:
		intro_background.afficher()

		if i>=55:
			Intro = 0
			Menu = 1
			pygame.mixer.music.play()
			pygame.display.flip()
		pygame.display.flip()

	#Intro vidéo
	#if not visionneuse:
		#Intro=1


	###########################
	###########MENU############
	###########################

	if Menu:
		menu_background.afficher()
		#play_button.afficher()
		#play_button.click()

		if i<=35:
			play_button.afficher()

		if i>=50:
			i=0

		play_button.click()

		if play_button.isClicked or touches[pygame.K_RETURN]:
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

		print("POS : ", perso.rect.x, perso.rect.y, ", CAM : ", perso.camerax, perso.cameray)
		#print("POS : ", mapgrid.X[perso.rect.y//64][perso.rect.x//64])
		#x+=1 #Game over programmer
		#Son du jeu


		actual_map = Maps[perso.map_id]
		perso.map = actual_map
		pygame.display.flip()
		#Definition de l'etat

		perso.map[0].afficher(perso.camerax,perso.cameray)
		perso.afficher()
		if perso.deplacement(warps= Warps)==1:
			print(perso.deplacement())




		for w in range(4):
			tab_vie[w].afficher()

		if x>=100:
			GameOver=1
			enJeu = 0
		# rafraichissement
		pygame.display.flip()


	##################################
	############GAME OVER#############
	##################################

	if GameOver:
		GAMEOVER.afficher()
		if touches[pygame.K_RETURN]:
			enJeu=1
			GameOver=0
		elif touches[pygame.K_SPACE]:
			GameOver=0
			Play=False
		# rafraichissement
		pygame.display.flip()


# Fin programme
pygame.quit()
quit()
