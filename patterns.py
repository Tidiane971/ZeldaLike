# patterns.py
# Contient des implémentations minimalistes de Command, Observer, Singleton
from Graphique.elements_graphique import *
#######################
# Command Pattern
#######################
class Command:
    def execute(self, perso, touches):
        pass

class MoveCommand(Command):
    def __init__(self, direction):
        self.direction = direction  # "haut", "bas", "gauche", "droite"

    def execute(self, perso, touches):
        # On peut agir directement sur le perso ou modifier ses entrées
        # Ici, on se contente de simuler la pression d'une touche directionnelle
        # C'est volontairement simplifié
        # On pourrait imaginer un mapping direction -> touches, mais on va faire simple
        # Juste pour montrer le concept
        pass

class AttackCommand(Command):
    def execute(self, perso, touches):
        # On pourrait, par exemple, déclencher l'attaque
        # Mais on va juste montrer l'idée
        # Dans la logique actuelle, l'attaque est déjà gérée dans perso.update_state()
        # Si on voulait vraiment l'appliquer, on pourrait modifier perso pour accepter une méthode perso.attack_command()
        pass

#######################
# Observer Pattern
#######################
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for obs in self.observers:
            obs.update(*args, **kwargs)

class Observer:
    def update(self, *args, **kwargs):
        pass

# Observateur simple pour la vie du perso
class HeartUIObserver(Observer):
    def __init__(self, tab_vie, fenetre, objet):
        self.tab_vie = tab_vie
        self.fenetre = fenetre
        self.objet = objet

    def update(self, vie):
        # Mise à jour de l'affichage des cœurs en fonction de la vie
        entier = int(str(vie//4)[0])
        valeur_virgule = int(str(((vie / 4) - entier)*4)[0])
        virgule = 1 if valeur_virgule != 0 else 0

        for k in range(3):
            self.tab_vie[k] = None

        # Coeurs pleins
        for k in range(entier):
            self.tab_vie[k] = ElementGraphique(self.objet["heart_0"], self.fenetre, x=10+50*(k), y=10)

        # Coeur partiel
        if virgule == 1:
            self.tab_vie[entier] = ElementGraphique(self.objet["heart_"+str(valeur_virgule)], self.fenetre, x=10+50*(entier), y=10)

#######################
# Singleton Pattern
#######################
class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
            # Initialise les ressources globales
            cls._instance.global_data = {}
        return cls._instance

    def get_global_data(self, key):
        return self.global_data.get(key, None)

    def set_global_data(self, key, value):
        self.global_data[key] = value


