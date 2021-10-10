#Code principal jeu
import pygame
import random
import time

#Code principal jeu
#testjjkjk
#modifier par tidiane
# Initialisation Jeu
pygame.init()

# Nom du jeu
pygame.display.set_caption("L'épopée_de_Lynk.exe")

# Définition fenêtre (à changer si besoin)
rés=(840,550)
fenetre=pygame.display.set_mode(rés)

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

	if touches[pygame.K_ESCAPE]: # Échap / Quitter
		Play=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			Play=False

	pass

# Fin programme
pygame.quit()
quit()
