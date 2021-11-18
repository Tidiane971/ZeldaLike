from moviepy.editor import *
import pygame

visionage=True

film = VideoFileClip('Film.mp4')

while visionage:

    #Skip
    if touches[pygame.K_ESCAPE]:
        visionage=False
    else:
        film.preview()

	#Quitter Jeu
    touches=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            visionage=False

pygame.quit()