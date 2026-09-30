from arbitre import Arbitre
from joueurs import Joueurs


class Jeu:

    def __init__(self):
        self.joueurs: list[Joueurs] = []
        self.arbitre = Arbitre()

    def initialiser(self, nom_premier=None, nom_second=None):
        if nom_premier is None:
            nom_premier = input("Nom du premier joueur : ").strip()
        if nom_second is None:
            nom_second = input("Nom du second joueur : ").strip()

        if not nom_premier:
            raise ValueError("Le nom du premier joueur ne peut pas être vide.")
        if not nom_second:
            raise ValueError("Le nom du second joueur ne peut pas être vide.")

        self.joueurs = [Joueurs(nom_premier), Joueurs(nom_second)]

    def est_fini(self):
        if len(self.joueurs) != 2:
            return False

        for joueur in self.joueurs:
            if joueur.nbr_jetons <= 0:
                return True

        return False

    def afficher_resultat(self):
        if len(self.joueurs) != 2:
            print("Le jeu n'est pas initialisé.")
            return

        print("Résultat courant :")
        for joueur in self.joueurs:
            joueur.afficher_score()

    def jouer_manche(self):
        if len(self.joueurs) != 2:
            raise RuntimeError("Le jeu doit être initialisé avant de jouer.")

        premier_joueur = self.joueurs[0]
        second_joueur = self.joueurs[1]

        premier_lancer = premier_joueur.jouer()
        second_lancer = second_joueur.jouer()
        transfert = self.arbitre.arbitrer(premier_lancer, second_lancer)

        premier_joueur.ajouter_jetons(transfert)
        second_joueur.ajouter_jetons(-transfert)

        return transfert

    def se_lancer(self):
        if len(self.joueurs) != 2:
            self.initialiser()

        while not self.est_fini():
            self.jouer_manche()

            premier_lancer = self.joueurs[0].dernier_lancer
            second_lancer = self.joueurs[1].dernier_lancer
            print(f"{self.joueurs[0].nom} lance {premier_lancer}.")
            print(f"{self.joueurs[1].nom} lance {second_lancer}.")
            self.afficher_resultat()

        for joueur in self.joueurs:
            if joueur.nbr_jetons > 0:
                print(f"{joueur.nom} a gagné.")
                return joueur

        return None


if __name__ == "__main__":
    jeu = Jeu()
    jeu.se_lancer()