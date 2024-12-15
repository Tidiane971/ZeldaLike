##STATE MACHINE

from Graphique.elements_graphique import ElementGraphique

class element_anime(ElementGraphique):
    def __init__(self, images, fenetre, x=0, y=0):
        super().__init__(images[0],fenetre, x, y)
        self.images = images
        self.delai = 2
        self.num_image = 0
        self.timer = 0

    def afficher(self):
        self.timer += 1
        if self.timer > self.delai:
            self.timer=0
            self.num_image += 1
            if self.num_image >= len(self.images):
                self.num_image = 0
            self.image=self.images[self.num_image]

        super().afficher()


#Direction d'animation
class element_anime_dir(element_anime):
    def __init__(self, images, fenetre, x=0, y=0):
        self.dico_images = images
        self.direction = "bas"
        self.old_direction = "bas"

        super().__init__(images[self.direction],fenetre, x,y)

    def afficher(self):
        if self.direction == self.old_direction :
            super().afficher()
        else :
            self.images = self.dico_images[self.direction]
            self.num_image = 0
            self.old_direction = self.direction
            super().afficher()
