# import cv2
# import pygame
# import constantes
#
# cap = cv2.VideoCapture('Film.mp4')
# success, img = cap.read()
# shape = img.shape[1::-1]
# wn = pygame.display.set_mode(shape)
# clock = pygame.time.Clock()
#
# while success:
#     clock.tick(30)
#     success, img = cap.read()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             success = False
#     if(img is not None):
#         wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
#         pygame.display.update()
#
# fenetre=pygame.display.set_mode((constantes.largeur,constantes.hauteur))
