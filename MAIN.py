#Code principal jeu
#Importation Fichier
from pnj_gestion import *
from coffre_gestion import *
from constantes import *
from textBank import *
from Fonction import *
from Warp import *
#from Film import *
from Map import *
from BG import *

#Importation module
import pygame.freetype
import pygame.mixer
import keyboard
import mapgrid
import pygame
import random
import time


#Initialisation Jeu
#Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")

#Appel horloge
temps=pygame.time.Clock()

#Définition musique
pygame.mixer.music.load("Source/Musique_&_Son/intro_theme1.ogg")


#--------LECTURE DES IMAGES
objet = lecture_objet()

#Image coeurs
v,pvie=0,0
tab_vie=[]
for i in range(4):
	vie= elementgraphique(objet["heart_"+str(v)],fenetre,x=10+50*i,y=10)
	tab_vie.append(vie)

#Image Lynk
perso = perso(objet["Lynk"],fenetre,x=152,y=243,camerax=CameraX,cameray=CameraY,map = actual_map, map_id = 0 )

#Image curseur
Choix=elementgraphique(objet["select"],fenetre,x=270,y=400)

korogu_tab=[]
#----------VARIABLES UTILES
i=0
Play=True
YES=True
leave=False
Intro,Menu,enJeu,enPause,flipper,GameOver=1,0,0,0,0,0

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
			#pygame.mixer.music.play()
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

		#Gestion start
		if i<=35:
			play_button.afficher()
		elif i>=50:
			i=0
		play_button.click()

		if play_button.isClicked or touches[pygame.K_RETURN]:
			Menu,x,v = 0,0,4
			enJeu = 1
			pygame.mixer.music.load("Source/Musique_&_Son/Village.ogg")
			# pygame.mixer.music.play()
			pygame.display.flip()


	############################
	############JEU#############
	############################

	if enJeu==1 and enPause==0:

		#Boost Perso
		if(touches[pygame.K_SPACE]):
			perso.vitesse = 16
		else:
			perso.vitesse = 6

		#print("POS : ", perso.rect.x, perso.rect.y, ", CAM : ", perso.camerax, perso.cameray)
		#print("WARP SORTIE GROTTE : ", Warps[2][0].rect.x, Warps[2][0].rect.y)
		#print("POS : ", mapgrid.X[perso.rect.y//64][perso.rect.x//64])

		#Gestion Map
		actual_map = Maps[perso.map_id]
		perso.map = actual_map


		#Affichage perso
		perso.map[0].afficher(perso.camerax,perso.cameray)
		perso.afficher()
		if perso.map_id in map_having_pnj:
			for pnj in pnj_liste[perso.map_id]:
				pnj.afficher(perso = perso)
		perso.map[1].afficher(perso.camerax,perso.cameray)


		#Gestion coffre
		if perso.map_id in map_having_coffre:
			for coffre in coffre_liste[perso.map_id]:
				coffre.afficher(perso=perso)

		#Gestion Dialogue
		if(not perso.inDialog):
			perso.deplacement(vie=perso.vie)
		perso.read(DB = DialogBoxes)
		perso.talk(PNG = pnj_liste)
		perso.open(COFFRES = coffre_liste)
		perso.warping()

		perso.inventaire.afficher()

		
		print("PV=", perso.vie)
		if x==2 and v>0:
			x=0
			pvie+=1
			perso.vie-=1
			vie=elementgraphique(objet["heart_"+str(pvie)],fenetre,x=10+50*(v-1),y=10)
			tab_vie[v-1]=vie
			if pvie==4: #Changement coeur
				v-=1
				pvie=0
				pass
		elif perso.vie<=0:
			#perso.dead(vie=perso.vie) ---- Animation mort raté
			GameOver=1
			enJeu = 0

		for w in range(4):
			tab_vie[w].afficher()


		#----------Activer Pause
		if keyboard.is_pressed('p'):
			enPause=1
			Bouj=True
			pygame.time.delay(190)

		while enJeu==1 and enPause==1:
			touches=pygame.key.get_pressed()

			#Animation Ecran
			flipper+=1
			if flipper<=75:
				Pause1.afficher()
			elif flipper<=125:
				Pause2.afficher()
			else:
				flipper=0

			#Gestion curseur
			i+=1
			if i<75 and Bouj==True:
				Choix.rect.x-=16
				Bouj=False
			elif i>=75 and i<=150 and Bouj==False:
				Choix.rect.x+=16
				Bouj=True
			elif i>150:
				i=0
			print(i)

			if touches[pygame.K_UP] and leave==False:
				leave=True
				Choix.rect.y-=35
			elif touches[pygame.K_DOWN] and leave==True:
				leave=False
				Choix.rect.y+=35

			Choix.afficher()

			#------GESTION ETAT
			#Quitter/Pause
			if keyboard.is_pressed('p') and leave==True:
				enPause=0
				pygame.time.delay(190)
			elif keyboard.is_pressed('p') and leave==False:
				enPause=0
				Play=False

			#Quitter Jeu
			if touches[pygame.K_ESCAPE]:
				enPause=0
				Play=False
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					enPause=0
					Play=False

			# rafraichissement
			pygame.display.flip()
			pass



		#gestion korogu
		#if i%1000=0:
		#	korogu = ennemi(objet["ennemi"][korogu],fenetre,x=152,y=243,)
		#	korogu_tab.append(korogu)
		#for i in korogu_tab:
			#i.afficher()

		#Gestion coeurs
		for w in range(4):
			tab_vie[w].afficher()


		#GameOver programmer
		#x+=1
		#if x>=100:
			#GameOver=1
			#enJeu = 0


	##################################
	############GAME OVER#############
	##################################

	if GameOver:
		print(YES)

		# Permuter / Afficher GameOver
		if YES==True:
			GAMEOVER1.afficher()
			if touches[pygame.K_RIGHT]:
				YES=False
		elif YES==False:
			GAMEOVER2.afficher()
			if touches[pygame.K_LEFT]:
				YES=True

		#------GESTION ETAT
		if keyboard.is_pressed('p') and YES==True:
			enJeu=1
			perso.vie=16
			GameOver=0
		elif keyboard.is_pressed('p') and YES==False:
			GameOver=0
			Play=False

	# rafraichissement
	pygame.display.flip()

# Fin programme
pygame.quit()
quit()
