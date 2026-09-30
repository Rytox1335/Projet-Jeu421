from dès import De
from lancer import Lancer

des = De()
Lancer = Lancer()

class Joueurs:
    def __init__(self,nom,nbr_jetons,lst_lancer, des):
        self.nom : str = nom
        self.nbr_jetons : int = nbr_jetons
        self.lst_lancer : list[int] = lst_lancer
        
        
    def lancer_des (self):
        for i in range(0,3):
            lancer =des.rouler(De)
            if i == 0:
                Lancer.face1 = lancer
                self.lst_lancer.append(lancer)
            elif i == 1 : 
                Lancer.face2 = lancer
                self.lst_lancer.append(lancer)
            else:
                Lancer.face3=lancer
                self.lst_lancer.append(lancer)
        return Lancer
                
    
    def retrait_points (self, coup):
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
                
    def __str__(self):
        return self.nbr_jetons
        
        