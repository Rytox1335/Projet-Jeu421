import random


class De:

    NB_FACES = 6

    def __init__(self):
        self.nb_faces: int = De.NB_FACES
        self.valeur: int | None = None

    def rouler(self):
        self.valeur = random.randint(1, self.nb_faces)
        return self.valeur

    def afficher(self):
        print(self.valeur)

    def __str__(self):
        return str(self.valeur)


