#PROGAMME PRINCIPAL
#Importation Fichier
from pnj_gestion import *
from coffre_gestion import *
from ennemi_gestion import *
from objet_gestion import *
from constantes import *
from textBank import *
from Fonction import *
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
entier = 3
virgule =  0
tab_vie=[]
for i in range(4):
	vie= elementgraphique(objet["heart_0"],fenetre,x=10+50*i,y=10)
	tab_vie.append(vie)

#Image Lynk
perso = perso(objet["Lynk"],fenetre,x=153,y=243,camerax=CameraX,cameray=CameraY,map = actual_map, map_id = 0 )
z=16
#Image curseur
Choix=elementgraphique(objet["select"],fenetre,x=270,y=400)

korogu_tab=[]

#----------VARIABLES UTILES
i=0
Play,YES=True,True
leave,Chanj=False,False
Intro,Menu,enJeu,Old_id,enPause,flipper,GameOver=1,0,0,0,0,0,0

#Boucle jeu
while Play:

	i+=1
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
			NOIR.afficher()
			Intro = 0
			pygame.display.flip()
			pygame.mixer.music.load("Source/Musique_&_Son/intro_theme2.ogg")
			pygame.mixer.music.play()
			import Film as Film
			Menu = 1
			pygame.mixer.music.load("Source/Musique_&_Son/intro_theme1.ogg")
			pygame.mixer.music.play()


	###########################
	###########MENU############
	###########################

	if Menu:
		menu_background.afficher()

		#Gestion start
		if i<=35:
			play_button.afficher()
		elif i>=50:
			i=0
		play_button.click()

		if play_button.isClicked or touches[pygame.K_RETURN]:
			Menu,x,v = 0,0,4
			enJeu = 1
			pygame.mixer.music.load("Source/Musique_&_Son/House_theme.ogg")
			pygame.mixer.music.play()
			pygame.display.flip()


	############################
	############JEU#############
	############################

	if enJeu==1 and enPause==0:

		#Boost Perso
		if keyboard.is_pressed('space'):
			perso.vitesse = 16
		else:
			perso.vitesse = 9

		#print("POS : ", perso.rect.x, perso.rect.y, ", CAM : ", perso.camerax, perso.cameray)
		#print("WARP SORTIE GROTTE : ", Warps[2][0].rect.x, Warps[2][0].rect.y)
		#print("POS : ", mapgrid.X[perso.rect.y//64][perso.rect.x//64])

		#Gestion Map
		actual_map = Maps[perso.map_id]
		perso.map = actual_map

		#Gestion Musique
		if Old_id!=perso.map_id:
			pygame.mixer.music.stop()
			Old_id=perso.map_id
			Chanj=True

		if Old_id==0 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/House_Theme.ogg")
		elif Old_id==1 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/Village.ogg")
		elif perso.map_id==2 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/Donjon_Theme.ogg")
		elif perso.map_id==3 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/Autre_Theme.ogg")
		elif perso.map_id==4 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/Autre_Theme.ogg")
		elif perso.map_id==5 and Chanj==True:
			pygame.mixer.music.load("Source/Musique_&_Son/Autre_Theme.ogg")
		elif perso.map_id==6 and Chanj == True:
			pygame.mixer.music.load("Source/Musique_&_Son/Boss_Theme.ogg")


		if Chanj==True:
			pygame.mixer.music.play()
			Chanj=False

		#Affichage perso
		perso.map[0].afficher(perso.camerax,perso.cameray)
		perso.afficher()
		if perso.map_id in map_having_pnj:
			for pnj in pnj_liste[perso.map_id]:
				pnj.afficher(perso = perso)
		perso.map[1].afficher(perso.camerax,perso.cameray)

		#Déplacer perso
		if(not perso.inDialog):
			perso.deplacement(vie=perso.vie, ennemiL=ennemi_liste[perso.map_id])

		if perso.map_id in map_having_ennemi and perso.map_id != 6:
			for ennemi in ennemi_liste[perso.map_id]:
				if ennemi.vie > 0:
					ennemi.afficher(perso=perso)
					ennemi.deplacement( perso = perso)
					ennemi.attaque(perso = perso)
				else:
					perso.map[2][ennemi.rect.y//64][ennemi.rect.x//64] =0
		else:
			for ennemi in ennemi_liste[perso.map_id]:
				if ennemi.vie > 0:
					ennemi.afficher(perso=perso)
					ennemi.deplacementBoss( perso = perso)
					ennemi.attaque(perso = perso)
				else:
					perso.map[2][ennemi.rect.y//64][ennemi.rect.x//64] =0


		if objet_dict["Collier"] in perso.inventaire.contenu and perso.map_id == 0:
			pnj_liste[0][0].text = ["Merci beaucoup fiston de m'avoir rapporter le collier"]
			perso.inventaire.contenu.remove(objet_dict["Collier"])

		#Gestion Dialogue
		perso.read(DB = DialogBoxes)
		perso.talk(PNG = pnj_liste)
		perso.open(COFFRES = coffre_liste)
		perso.warping(objet_dict = objet_dict)


		#Gestion coffre
		if perso.map_id in map_having_coffre:
			if perso.map_id == 6:
				for ennemi in ennemi_liste[perso.map_id]:
					if ennemi.vie <= 0:
						for coffre in coffre_liste[perso.map_id]:
							coffre.afficher(perso=perso)
			else:
				for coffre in coffre_liste[perso.map_id]:
					coffre.afficher(perso=perso)

		#Gestion ennemis







		#Gestion Inventaire
		perso.inventaire.afficher()
		mouse_pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				perso.inventaire.consume(perso = perso , pos = mouse_pos)


	    #GESTION DE VIE
		entier = int(str(perso.vie//4)[0])
		valeur_virgule =  int(str(((perso.vie / 4) - entier) *4)[0])

		if(valeur_virgule!=0):
			virgule = 1
		else:
			virgule = 0
		vide = entier + virgule

		for k in range(entier):
			tab_vie[k] = elementgraphique(objet["heart_0"],fenetre,x=10+50*(k),y=10)

		for i in range(entier, entier+virgule):
			tab_vie[i] = elementgraphique(objet["heart_"+str(valeur_virgule)],fenetre,x=10+50*(i),y=10)

		for j in range(entier+virgule,4):
			tab_vie[j] = elementgraphique(objet["heart_4"],fenetre,x=10+50*(j),y=10)

		for w in range(4):
			tab_vie[w].afficher()

		if perso.vie<=0:


			GameOver=1
			enJeu = 0





		# if perso.vie<=0:


		#if perso.vie<=0:

		#Gestion Dégat
		#if x==2 and v>0:
			#x=0
			#pvie+=1
			#perso.vie-=1 #perso.vie-Ennemi.attak
			#vie=elementgraphique(objet["heart_"+str(pvie)],fenetre,x=10+50*(v-1),y=10)
			#tab_vie[v-1]=vie
			#if pvie==4: #Changement coeur
				#v-=1
				#pvie=0
				#pass









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
			actual_map = 0
			perso.map_id = 0
			perso.rect.x = 152
			perso.rect.y = 243

			GameOver=0
		elif keyboard.is_pressed('p') and YES==False:
			GameOver=0
			Play=False

	# rafraichissement
	pygame.display.flip()

# Fin programme
pygame.quit()
quit()
