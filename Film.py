from moviepy.editor import *
import pygame

visionage=True
film = VideoFileClip('Film.mp4')
film.preview()

visionage=False

pygame.quit()