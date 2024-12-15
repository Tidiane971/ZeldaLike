import pygame
import keyboard
from Utils.constantes import *
class GameState:
    def __init__(self, context):
        self.context = context
    def on_enter(self): pass
    def on_exit(self): pass
    def handle_input(self, touches, events): pass
    def update(self): pass
    def render(self, fenetre): pass

class GameContext:
    def __init__(self, initial_state):
        self.state = initial_state
    def change_state(self, new_state):
        self.state.on_exit()
        self.state = new_state
        self.state.on_enter()
    def handle_input(self, touches, events):
        self.state.handle_input(touches, events)
    def update(self):
        self.state.update()
    def render(self, fenetre):
        self.state.render(fenetre)

# IntroState correspond à Intro==1 dans ton code
class IntroState(GameState):
    def on_enter(self):
        self.gm = self.context.gm
        self.i = 0
        self.Intro = 1
        self.Menu = 0
        # Musique intro déjà chargée
        # pygame.mixer.music.load("assets/Source/Musique_&_Son/intro_theme1.ogg") # déjà loadé dans main
        # pygame.mixer.music.play() # déjà lancé dans main
    def on_exit(self):
        pass

    def handle_input(self, touches, events):
        # Rien de particulier, on passe automatiquement au menu après i>=55
        pass

    def update(self):
        self.i += 1
        if self.i>=55:
            # Passage automatique au menu comme dans ton code
            from states import MenuState
            self.context.change_state(MenuState(self.context))

    def render(self, fenetre):
        intro_background = self.gm.get_global_data("intro_background")
        NOIR = self.gm.get_global_data("NOIR")
        intro_background.afficher()
        if self.i>=55:
            NOIR.afficher()

# MenuState correspond à Menu==1 dans ton code
class MenuState(GameState):
    def on_enter(self):
        self.gm = self.context.gm
        self.i = 0
        self.Menu=1
        self.play_button = self.gm.get_global_data("play_button")
        self.menu_background = self.gm.get_global_data("menu_background")

        pygame.mixer.music.load("assets/Source/Musique_&_Son/intro_theme2.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.load("assets/Source/Musique_&_Son/intro_theme1.ogg")
        pygame.mixer.music.play()

    def on_exit(self):
        pass

    def handle_input(self, touches, events):
        # Si on clique ou Entrée → passage au jeu (PlayState)
        if self.play_button.isClicked or touches[pygame.K_RETURN]:
            from states import PlayState
            self.context.change_state(PlayState(self.context))

    def update(self):
        self.i += 1
        if self.i<=35:
            self.play_button.afficher()
        elif self.i>=50:
            self.i=0
        self.play_button.click()

    def render(self, fenetre):
        self.menu_background.afficher()
        if self.i<=35:
            self.play_button.afficher()

# PlayState correspond à enJeu==1 et enPause==0
class PlayState(GameState):
    def on_enter(self):
        self.gm = self.context.gm
        self.enJeu=1
        self.enPause=0
        self.GameOver=0
        self.Intro=0
        self.Menu=0
        self.Chanj = False
        self.Old_id=0
        self.perso = self.gm.get_global_data("perso")
        self.tab_vie = self.gm.get_global_data("tab_vie")
        self.map_having_pnj = self.gm.get_global_data("map_having_pnj")
        self.map_having_coffre = self.gm.get_global_data("map_having_coffre")
        self.map_having_ennemi = self.gm.get_global_data("map_having_ennemi")
        self.ennemi_liste = self.gm.get_global_data("ennemi_liste")
        self.coffre_liste = self.gm.get_global_data("coffre_liste")
        self.pnj_liste = self.gm.get_global_data("pnj_liste")
        self.objet_dict = self.gm.get_global_data("objet_dict")
        self.DialogBoxes = self.gm.get_global_data("DialogBoxes")
        self.Transi = self.gm.get_global_data("Transi")
        self.Maps = self.gm.get_global_data("Maps")
        self.clock = pygame.time.Clock()

    def on_exit(self):
        pass

    def handle_input(self, touches, events):
        # Boost Perso
        if keyboard.is_pressed('space'):
            self.perso.vitesse = 16
        else:
            self.perso.vitesse = 9

        if touches[pygame.K_ESCAPE]:
            # Retour au menu si on veut
            from states import MenuState
            self.context.change_state(MenuState(self.context))

        # Pause (p)
        if keyboard.is_pressed('p'):
            from states import PauseState
            self.context.change_state(PauseState(self.context))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.perso.inventaire.consume(perso=self.perso, pos=mouse_pos)

    def update(self):
        self.clock.tick(30)
        touches=pygame.key.get_pressed()

        # Gestion Map
        actual_map = self.Maps[self.perso.map_id]
        self.perso.map = actual_map
        

        # Gestion Musique
        if self.Old_id!=self.perso.map_id:
            pygame.mixer.music.stop()
            self.Old_id=self.perso.map_id
            self.Chanj=True

        if self.Old_id==0 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/House_Theme.ogg")
        elif self.Old_id==1 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Village.ogg")
        elif self.perso.map_id==2 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Donjon_Theme.ogg")
        elif self.perso.map_id==3 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Autre_Theme.ogg")
        elif self.perso.map_id==4 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Autre_Theme.ogg")
        elif self.perso.map_id==5 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Autre_Theme.ogg")
        elif self.perso.map_id==6 and self.Chanj==True:
            pygame.mixer.music.load("assets/Source/Musique_&_Son/Boss_Theme.ogg")

        if self.Chanj==True:
            pygame.mixer.music.play()
            self.Chanj=False

        # FSM Perso
        self.perso.update_state(touches)
        if (not self.perso.inDialog):
            self.perso.deplacement(touches)
            self.perso.attaque(touches, self.ennemi_liste[self.perso.map_id], self.map_having_ennemi)

        if self.perso.map_id in self.map_having_ennemi:
            for ennemi in self.ennemi_liste[self.perso.map_id]:
                ennemi.set_map(self.perso.map)
                if ennemi.vie > 0:
                    ennemi.deplacement(perso=self.perso)
                    ennemi.attaque(perso=self.perso)
                else:
                    self.perso.map[2][ennemi.rect.y//64][ennemi.rect.x//64]=0


        # Collier
        if self.objet_dict["Collier"] in self.perso.inventaire.contenu and self.perso.map_id == 0:
            self.pnj_liste[0][0].text = ["Merci beaucoup fiston de m'avoir rapporter le collier"]
            self.perso.inventaire.contenu.remove(self.objet_dict["Collier"])

        # Dialogue
        self.perso.read(self.DialogBoxes)
        self.perso.talk(self.pnj_liste)
        self.perso.open(self.coffre_liste)
        self.perso.warping.warp(self.objet_dict, self.Transi)

        # Game Over
        if self.perso.vie<=0:
            from states import GameOverState
            self.context.change_state(GameOverState(self.context))

    def render(self, fenetre):
        perso=self.perso
        # Affichage carte et perso
        perso.map[0].afficher(perso.camerax,perso.cameray)
        perso.afficher()
        if perso.map_id in self.map_having_pnj:
            for pnj in self.pnj_liste[perso.map_id]:
                pnj.afficher(perso = perso)
        perso.map[1].afficher(perso.camerax,perso.cameray)

        # Affichage ennemis (sans déplacement ici!)
        if perso.map_id in self.map_having_ennemi:
            for ennemi in self.ennemi_liste[perso.map_id]:
                if ennemi.vie > 0:
                    ennemi.afficher(perso=perso)

        # Coffres
        if perso.map_id in self.map_having_coffre:
            if perso.map_id == 6:
                for ennemi in self.ennemi_liste[perso.map_id]:
                    if ennemi.vie <=0:
                        for coffre in self.coffre_liste[perso.map_id]:
                            coffre.afficher(perso=perso)
            else:
                for coffre in self.coffre_liste[perso.map_id]:
                    coffre.afficher(perso=perso)

        

        # Inventaire
        perso.inventaire.afficher()

        # Coeurs (Observer)
        for w in range(3):
            if self.tab_vie[w] is not None:
                self.tab_vie[w].afficher()

        if perso.inDialog:
        # Afficher la boîte de dialogue
            rectBox = (80, 400)
            boxImage = pygame.image.load("assets/Source/Autre/dialog_box.png")
            boxImage = pygame.transform.scale(boxImage, (715, 144))
            fenetre.blit(boxImage, rectBox)

            # Afficher chaque ligne de dialogue
            # Assure-toi que myfont est accessible (le même myfont que dans ton code)
            # Si myfont est global, importe-le ou mets-le dans GameManager et récupère-le
            global myfont
            y_offset = 452
            for line in perso.dialog_lines:
                myfont.render_to(fenetre, (152, y_offset), line, (0,0,0))
                y_offset += 20


# PauseState correspond à quand enPause==1
class PauseState(GameState):
    def on_enter(self):
        self.gm = self.context.gm
        self.enPause=1
        self.flipper=0
        self.leave=False
        self.i=0
        self.Bouj=True
        self.Choix = self.gm.get_global_data("Choix")
        self.Pause1 = self.gm.get_global_data("Pause1")
        self.Pause2 = self.gm.get_global_data("Pause2")
    def on_exit(self):
        pass

    def handle_input(self, touches, events):
        # Navigation dans le menu pause
        if touches[pygame.K_UP] and self.leave==False:
            self.leave=True
            self.Choix.rect.y-=35
        elif touches[pygame.K_DOWN] and self.leave==True:
            self.leave=False
            self.Choix.rect.y+=35

        import keyboard
        if keyboard.is_pressed('p') and self.leave==True:
            from states import PlayState
            self.context.change_state(PlayState(self.context))
        elif keyboard.is_pressed('p') and self.leave==False:
            from states import MenuState
            self.context.change_state(MenuState(self.context))

        if touches[pygame.K_ESCAPE]:
            from states import MenuState
            self.context.change_state(MenuState(self.context))

    def update(self):
        self.flipper+=1
        self.i+=1
        if self.i<75 and self.Bouj==True:
            self.Choix.rect.x-=16
            self.Bouj=False
        elif self.i>=75 and self.i<=150 and self.Bouj==False:
            self.Choix.rect.x+=16
            self.Bouj=True
        elif self.i>150:
            self.i=0

    def render(self, fenetre):
        if self.flipper<=75:
            self.Pause1.afficher()
        elif self.flipper<=125:
            self.Pause2.afficher()
        else:
            self.flipper=0
        self.Choix.afficher()

# GameOverState correspond à GameOver==1
class GameOverState(GameState):
    def on_enter(self):
        self.gm = self.context.gm
        self.GAMEOVER1 = self.gm.get_global_data("GAMEOVER1")
        self.GAMEOVER2 = self.gm.get_global_data("GAMEOVER2")
        self.YES=True
        self.perso = self.gm.get_global_data("perso")

    def on_exit(self):
        pass

    def handle_input(self, touches, events):
        import keyboard
        if touches[pygame.K_RIGHT] and self.YES==True:
            self.YES=False
        elif touches[pygame.K_LEFT] and self.YES==False:
            self.YES=True

        if keyboard.is_pressed('p') and self.YES==True:
            # Relancer le jeu
            self.perso.set_vie(12)
            self.perso.map_id=0
            self.perso.rect.x=152
            self.perso.rect.y=243
            from states import PlayState
            self.context.change_state(PlayState(self.context))
        elif keyboard.is_pressed('p') and self.YES==False:
            from states import MenuState
            self.context.change_state(MenuState(self.context))

    def update(self):
        pass

    def render(self, fenetre):
        if self.YES==True:
            self.GAMEOVER1.afficher()
        else:
            self.GAMEOVER2.afficher()
