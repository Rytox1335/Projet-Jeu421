import random


class De:
    """Un dé à 6 faces (le nombre de faces est fixe pour ce jeu)."""

    NB_FACES = 6

    def __init__(self):
        # Valeur courante (face supérieure). On démarre sur 1 avant le premier lancer.
        self.valeur = 1

    def rouler(self):
        """Lance le dé : tire une face au hasard et la retourne."""
        self.valeur = random.randint(1, De.NB_FACES)
        return self.valeur

    def afficher(self):
        """Affiche la valeur courante du dé."""
        print(self.valeur)

    def __str__(self):
        return str(self.valeur)


# Petit test : ne s'exécute que si on lance directement ce fichier
if __name__ == "__main__":
    d = De()
    for _ in range(5):
        d.rouler()
        d.afficher()
