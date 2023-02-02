from datetime import datetime
from voiture import Voiture
class Agence:
    def __init__(self):
        self.voitures = []

    def ajouter_voiture(self, voiture):
     if self.rechercher_voiture_par_matricule(voiture.matricule):
        print("La voiture avec la matricule " + voiture.matricule + " existe déjà.")
        return
     self.voitures.append(voiture)

    def supprimer_voiture(self, matricule):
        for i, v in enumerate(self.voitures):
            if v.matricule == matricule:
                del self.voitures[i]
                return True
        return False

    def rechercher_voiture_par_matricule(self, matricule):
        for v in self.voitures:
            if v.matricule == matricule:
                print("voiture trouvez")
                return True
        print("voiture non trouvez")
        return False

    def afficher_voitures(self):
        for v in self.voitures:
            v.afficher_voiture()

    def trier_selon_date_circulation(self):
        self.voitures.sort(key=lambda x: x.date_circulation)

    def get_voiture_plus_recente(self):
        self.trier_selon_date_circulation()
        print("La voiture la plus récente est:")
        self.voitures[-1].afficher_voiture()

    def get_voiture_plus_ancienne(self):
        self.trier_selon_date_circulation()
        print("La voiture la plus ancienne est:")
        self.voitures[0].afficher_voiture()      

