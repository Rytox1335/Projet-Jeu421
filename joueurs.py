from dès import De
from lancer import Lancer

class Joueurs:
    def __init__(self, nom, nbr_jetons=11):
        self.nom: str = nom
        self.nbr_jetons: int = nbr_jetons
        self.des: list[De] = [De(), De(), De()]
        self.dernier_lancer: Lancer | None = None

    def jouer(self):
        valeurs = [de.rouler() for de in self.des]
        self.dernier_lancer = Lancer(valeurs)
        return self.dernier_lancer

    def lancer_des(self):
        return self.jouer()

    def mettre_a_jour_score(self, coup):
        match coup:
            case "421":
                self.nbr_jetons -= 8
            case "brelanAS":
                self.nbr_jetons -= 7
            case "brelan":
                self.nbr_jetons -= 3
            case "suite":
                self.nbr_jetons -= 2
            case "autre":
                self.nbr_jetons -= 1

    def afficher_score(self):
        print(f"{self.nom} : {self.nbr_jetons} jetons")

    def retrait_points(self, coup):
        self.mettre_a_jour_score(coup)

    def __str__(self):
        return f"{self.nom} : {self.nbr_jetons} jetons"
                        

