import random


class De:

    NB_FACES = 6

    def __init__(self):
        self.valeur : int = None

    def rouler(self):
        self.valeur = random.randint(1, De.NB_FACES)
        return self.valeur

    def afficher(self):
        print(self.valeur)

    def __str__(self):
        return str(self.valeur)


