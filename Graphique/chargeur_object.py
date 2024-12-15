import pygame


def lecture_objet():
    def load_image(path, size):
        """Utility to load and scale images."""
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, size)

    def load_animation(base_path, count, size, prefix="", suffix=""):
        """Utility to load animations (sequence of images)."""
        return [load_image(f"{base_path}{prefix}{i}{suffix}.png", size) for i in range(count)]

    objet = {}

    # Curseur
    objet["select"] = load_image("assets/Source/Autre/cursor/select.png", (25, 25))

    # Coeurs
    for i in range(5):
        objet[f"heart_{i}"] = load_image(f"assets/Source/Lynk/heart/heart_{i}.png", (52, 52))

    # Animation Lynk
    objet["Lynk"] = {}
    directions = ["bas", "droite", "gauche", "haut"]
    for direction in directions:
        objet["Lynk"][f"stand_{direction}"] = load_animation(
            f"assets/Source/Lynk/Lynk_stand_{direction}_", 4, (51, 51)
        )

    objet["Lynk"]["droite"] = load_animation("assets/Source/Lynk/Lynk_walk_droite_", 10, (51, 51))
    objet["Lynk"]["gauche"] = load_animation("assets/Source/Lynk/Lynk_walk_gauche_", 10, (51, 51))
    objet["Lynk"]["haut"] = load_animation("assets/Source/Lynk/Lynk_walk_haut_", 10, (51, 51))
    objet["Lynk"]["bas"] = load_animation("assets/Source/Lynk/Lynk_walk_bas_", 8, (51, 51))

    # Animation attaque épée
    attack_directions = ["bas", "droite", "gauche", "haut"]
    attack_counts = {"bas": 6, "droite": 7, "gauche": 7, "haut": 6}
    for direction in attack_directions:
        objet["Lynk"][f"hit_{direction}"] = load_animation(
            f"assets/Source/Lynk/tape/LINKtape{direction}_", attack_counts[direction], (102, 102)
        )

    # Animation mort
    objet["Lynk"]["dead"] = load_animation("assets/Source/Lynk/Lynk_dead_", 4, (51, 51))

    # Image korogu
    objet["ennemi"] = {"korogu": {}}
    for direction in directions:
        objet["ennemi"]["korogu"][direction] = load_animation(
            f"assets/Source/Enemy/korogu/korogu_walk_{direction}_", 4, (52, 52)
        )

    # Image Boss
    boss_image = load_image("assets/Source/PNJ/Boss/boss_all.png", (110, 110))
    objet["ennemi"]["boss"] = {direction: [boss_image] for direction in directions}

    return objet


