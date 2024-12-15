from Graphique.elements_graphique import *
import keyboard
import pygame


class Inventaire(ElementGraphique):
    def __init__(self, fenetre, perso):
        self.perso = perso
        self.x = 450
        self.y = 90
        self.image = pygame.image.load("assets/Source/Lynk/Inventaire/INVENTAIRE2.png")
        super().__init__(self.image, fenetre, self.x, self.y)
        self.contenu = []
        self.open = False
        self.slot = self._initialiser_slots(fenetre)

    def _initialiser_slots(self, fenetre):
        positions = [
            (469, 319), (529, 319), (582, 319), (638, 319), (694, 319),
            (469, 370), (525, 370), (582, 370), (636, 370), (694, 370),
            (469, 421), (525, 421), (582, 421), (638, 421), (694, 421),
        ]
        return {
            f"slot{i+1}": ElementGraphique(
                image=pygame.image.load("assets/Source/Map/slot.png"),
                fenetre=fenetre,
                x=pos[0],
                y=pos[1],
            )
            for i, pos in enumerate(positions)
        }

    def afficher(self):
        if keyboard.is_pressed("e"):
            self.open = not self.open
      
            pygame.time.delay(120)

        if self.open:
            self.fenetre.blit(self.image, (self.rect.x, self.rect.y))
            for i, item in enumerate(self.contenu):
                slot = self.slot[f"slot{i+1}"]
                item.image.rect.x = slot.rect.x
                item.image.rect.y = slot.rect.y
                item.image.afficher()

    def consume(self, perso, pos):
        if self.open and perso.vie < 16:
            for slot_name, slot in self.slot.items():
                if slot.rect.collidepoint(pos) and len(self.contenu) > 0:
                    index = int(slot_name[4:]) - 1
                    if self.contenu[index].nom == "Une Potion de Heal":
                        perso.vie += 2
                        self.contenu.pop(index)
                        break
