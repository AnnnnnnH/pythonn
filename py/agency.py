from datetime import datetime
import numpy as np
from voiture import Voiture

class Agence:
    def __init__(self):
        self.voitures = []

    # ... Other methods ...

    def transformer_voiture(self):
        self.voitures = [Voiture(*v) for v in self.voitures]

    def calcul_distances(self, voiture):
        features = np.array([(v.date_circulation - voiture.date_circulation).days,
                             v.kilometrage,
                             v.cylindrage] for v in self.voitures)
        distances = np.linalg.norm(features - [voiture.date_circulation, voiture.kilometrage, voiture.cylindrage], axis=1)
        return distances

    def trier_voitures(self, distances):
        self.voitures = [v for _, v in sorted(zip(distances, self.voitures), key=lambda x: x[0])]

    def afficher_tri(self, indice):
        for i, v in enumerate(self.voitures[:indice]):
            v.afficher_voiture()

    def rechercher_voitures_par_similarite(self):
        voiture = Voiture()
        voiture.saisir_voiture()
        distances = self.calcul_distances(voiture)
        self.trier_voitures(distances)
        self.afficher_tri(1)

if __name__ =="__main__" :
    agency = Agence()

    # Add some example cars to the list of cars
    agency.voitures = [["m1", "toyotz", datetime.strptime("2001-01-01", "%Y-%m-%d"), 100000, 1000],
                       ["m", "bmw", datetime.strptime("2022-01-01", "%Y-%m-%d"), 200000, 2000],
                       ["m", "AUdi", datetime.strptime("2019-01-01", "%Y-%m-%d"), 300000, 3000]]

    # Transform the list of cars into `Voiture` objects
    agency.transformer_voiture()
    # Search for cars similar to an input car
    agency.rechercher_voitures_par_similarite()

# 