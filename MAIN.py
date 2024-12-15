import pygame
import pygame.mixer
import pygame.freetype
from Utils.constantes import *
from ModuleGestion.pnj_gestion import *
from ModuleGestion.coffre_gestion import *
from ModuleGestion.ennemi_gestion import *
from ModuleGestion.objet_gestion import *
from Graphique.elements_graphique import *
from ModuleGestion.map_gestion import *
from Utils.loaded_image import *
from Personnage.perso import *
from patterns import GameManager
from states import GameContext, IntroState
from Utils.constantes import * # importe fenetre, pnj_liste, etc.

pygame.init()
pygame.display.set_caption("L'épopée_de_Lynk.exe")

# Chargement objets
objet = lecture_objet()

# Charger images
intro_background = ElementGraphique(background_intro, fenetre)
NOIR = ElementGraphique(noir, fenetre)
menu_background = ElementGraphique(background_img, fenetre)
play_button = button(play_button_img, fenetre)
play_button.rect.x=135
play_button.rect.y=95
Pause1 = ElementGraphique(pause1, fenetre)
Pause2 = ElementGraphique(pause2, fenetre)
GAMEOVER1 = ElementGraphique(gameover, fenetre)
GAMEOVER2 = ElementGraphique(gameover2, fenetre)

# Tab vie
tab_vie=[]
for i in range(3):
    vie= ElementGraphique(objet["heart_0"],fenetre,x=10+50*i,y=10)
    tab_vie.append(vie)

# Perso
perso = Perso(objet["Lynk"],fenetre,x=153,y=243,camerax=CameraX,cameray=CameraY,map = actual_map, map_id = 0)
Choix=ElementGraphique(objet["select"],fenetre,x=270,y=400)

# Initialiser GameManager
gm = GameManager()
gm.set_global_data("fenetre", fenetre)
gm.set_global_data("objet", objet)
gm.set_global_data("intro_background", intro_background)
gm.set_global_data("NOIR", NOIR)
gm.set_global_data("menu_background", menu_background)
gm.set_global_data("play_button", play_button)
gm.set_global_data("Pause1", Pause1)
gm.set_global_data("Pause2", Pause2)
gm.set_global_data("GAMEOVER1", GAMEOVER1)
gm.set_global_data("GAMEOVER2", GAMEOVER2)
gm.set_global_data("tab_vie", tab_vie)
gm.set_global_data("perso", perso)
gm.set_global_data("pnj_liste", pnj_liste)
gm.set_global_data("coffre_liste", coffre_liste)
gm.set_global_data("ennemi_liste", ennemi_liste)
gm.set_global_data("map_having_pnj", map_having_pnj)
gm.set_global_data("map_having_coffre", map_having_coffre)
gm.set_global_data("map_having_ennemi", map_having_ennemi)
gm.set_global_data("DialogBoxes", DialogBoxes)
gm.set_global_data("Transi", Transi)
gm.set_global_data("Maps", Maps)
gm.set_global_data("Choix", Choix)
gm.set_global_data("objet_dict", objet_dict)

# Musique d'intro
pygame.mixer.music.load("assets/Source/Musique_&_Son/intro_theme1.ogg")
pygame.mixer.music.play()

# Création de l'état initial et du contexte sans appeler on_enter() trop tôt
initial_state = IntroState(None)
context = GameContext(initial_state)

# Maintenant que context est créé, on peut attribuer context et gm à l’état, puis appeler on_enter()
context.state.context = context
context.state.context.gm = gm
context.state.on_enter()  # Appel manuel maintenant que gm et context sont prêts

clock = pygame.time.Clock()
Play = True

while Play:
    clock.tick(30)
    touches = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            Play=False

    context.handle_input(touches, events)
    context.update()
    context.render(fenetre)

    pygame.display.flip()

pygame.quit()
quit()