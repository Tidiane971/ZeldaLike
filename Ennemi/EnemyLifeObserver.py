from patterns import Observer

class EnemyLifeObserver(Observer):
    def update(self, vie):
        print(f"L'ennemi a maintenant {vie} points de vie.")
