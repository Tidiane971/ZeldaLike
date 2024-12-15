from Graphique.elements_graphique import ElementGraphique

class Map(ElementGraphique):
    def __init__(self,image,fenetre,x=0,y=0):
        super().__init__(image,fenetre,x,y)

    def afficher(self, camerax, cameray):
        self.fenetre.blit(self.image, (self.rect.x-camerax, self.rect.y -cameray))
