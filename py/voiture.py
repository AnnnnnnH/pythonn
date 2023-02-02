from datetime import datetime
class Voiture:
    def __init__(self, matricule="", marque="", date_circulation=datetime.now(), kilometrage="", cylindrage=""):
        self.matricule = matricule
        self.marque = marque
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindrage = cylindrage

    def afficher_voiture(self):
         print("{} | {} | {} | {} | {}".format(str(self.matricule), self.marque, self.date_circulation.strftime("%Y-%m-%d"), str(self.kilometrage), str(self.cylindrage)))
    def saisir_voiture(self):
        self.matricule = input("Enter matricule: ")
        self.marque = input("Enter marque: ")
        self.date_circulation = input("Enter date_circulation (yyyy-mm-dd): ")
        if self.date_circulation == "":
            self.date_circulation = datetime.now()
        else:
            self.date_circulation = datetime.strptime(self.date_circulation, "%Y-%m-%d")
        self.kilometrage = input("Enter kilometrage: ")
        self.cylindrage = input("Enter cylindrage: ")
        

        

if __name__ =="__main__" :
        v = Voiture()
        v.saisir_voiture()
        v.afficher_voiture()
