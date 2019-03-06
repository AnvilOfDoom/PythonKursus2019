#klasse til opgave 1
class Materiale():
    """En klasse  til at beskrive biblioteksmateriale"""
    def __init__(self, idnr:int, titel, aarstal:int, antal:int=1):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antal_udlaan = 0
        self.aarstal = aarstal

    def toString(self):
        print("Titel og årstal: " + self.titel + " (" + str(self.aarstal) + (")") +
              "\nid: " + str(self.idnr) +
              "\nAntal kopier: " + str(self.antal) +
              "\nAntal udlånte kopier: " + str(self.antal_udlaan))

#klasser til opgave 2

class Bog(Materiale):
    """En child class til Materiale til at beskrive bøger"""
    def __init__(self, idnr, titel, aarstal):
        super().__init__(idnr, titel, aarstal)


class Film(Materiale):
    """En child class til Materiale til at beskrive film"""