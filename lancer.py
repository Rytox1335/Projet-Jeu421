class Lancer:

    def __init__(self, valeurs: list[int] | None = None):
        self.valeurs: list[int] = []
        if valeurs is not None:
            self.enregistrer(valeurs)

    def enregistrer(self, valeurs: list[int]) -> None:
        valeurs_enregistrees = list(valeurs)

        if len(valeurs_enregistrees) != 3:
            raise ValueError("Un lancer doit contenir trois valeurs comprises entre 1 et 6.")

        for valeur in valeurs_enregistrees:
            if valeur < 1 or valeur > 6:
                raise ValueError("Un lancer doit contenir trois valeurs comprises entre 1 et 6.")

        self.valeurs = valeurs_enregistrees

    def trier(self, decroissant: bool = True) -> list[int]:
        nombre_valeurs = len(self.valeurs)

        for indice in range(nombre_valeurs):
            for position in range(nombre_valeurs - indice - 1):
                valeur_actuelle = self.valeurs[position]
                valeur_suivante = self.valeurs[position + 1]

                if decroissant:
                    if valeur_actuelle < valeur_suivante:
                        self.valeurs[position] = valeur_suivante
                        self.valeurs[position + 1] = valeur_actuelle
                else:
                    if valeur_actuelle > valeur_suivante:
                        self.valeurs[position] = valeur_suivante
                        self.valeurs[position + 1] = valeur_actuelle

        return self.valeurs

    def est_421(self):
        if len(self.valeurs) != 3:
            return False

        valeurs_triees = sorted(self.valeurs)
        if valeurs_triees[0] != 1:
            return False
        if valeurs_triees[1] != 2:
            return False
        if valeurs_triees[2] != 4:
            return False

        return True

    def est_brelan(self):
        if len(self.valeurs) != 3:
            return False

        premiere_valeur = self.valeurs[0]
        deuxieme_valeur = self.valeurs[1]
        troisieme_valeur = self.valeurs[2]

        if premiere_valeur != deuxieme_valeur:
            return False
        if deuxieme_valeur != troisieme_valeur:
            return False

        return True

    def est_brelan_de(self, valeur):
        if not self.est_brelan():
            return False
        if self.valeurs[0] != valeur:
            return False

        return True

    def est_deux_as(self):
        nombre_as = 0
        for valeur in self.valeurs:
            if valeur == 1:
                nombre_as += 1

        if nombre_as != 2:
            return False

        return True

    def est_deux_as_et(self, valeur):
        if not self.est_deux_as():
            return False
        if valeur == 1:
            return False

        for valeur_lancee in self.valeurs:
            if valeur_lancee == valeur:
                return True

        return False

    def est_suite(self):
        if len(self.valeurs) != 3:
            return False

        valeurs_triees = sorted(self.valeurs)
        premiere_valeur = valeurs_triees[0]
        deuxieme_valeur = valeurs_triees[1]
        troisieme_valeur = valeurs_triees[2]

        if deuxieme_valeur != premiere_valeur + 1:
            return False
        if troisieme_valeur != deuxieme_valeur + 1:
            return False

        return True

    def __str__(self):
        return str(self.valeurs)

