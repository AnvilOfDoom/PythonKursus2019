#klasse til opgave 1
import re #til opgave 5

class Materiale():
    """En klasse  til at beskrive biblioteksmateriale"""
    def __init__(self, idnr:int, titel, aarstal:int, antal:int=1):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antal_udlaan = 0
        self.aarstal = aarstal

    def toString(self): #opgave 1
        print("Titel og årstal: " + self.titel + " (" + str(self.aarstal) + (")") +
              "\nid: " + str(self.idnr) +
              "\nAntal kopier: " + str(self.antal) +
              "\nAntal udlånte kopier: " + str(self.antal_udlaan))

    def kanUdlaane(self):   #opgave 5
        """Tjekker om der er flere kopier af materialet på lager, som kan udlånes"""
        if self.antal > self.antal_udlaan:
            return True
        else:
            return False

    def udlaan(self):   #opgave 5
        """Øger antal_udlaan med 1"""
        self.antal_udlaan += 1

    def matchTitle(self, search):
        return re.search(search, self.titel)


#klasser til opgave 2

class Bog(Materiale):
    """En child class til Materiale til at beskrive bøger"""
    def __init__(self, idnr, titel, aarstal, antalsider:int, forfatter, antal:int=1):
        super().__init__(idnr, titel, aarstal, antal=antal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def toString(self):
        """Udskriver beskrivelse af bogen"""
        print("Titel og årstal: " + self.titel + " (" + str(self.aarstal) + (")") +
              "\nForfatter: " + self.forfatter +
              "\nid: " + str(self.idnr) +
              "\nAntal kopier: " + str(self.antal) +
              "\nAntal udlånte kopier: " + str(self.antal_udlaan) +
              "\nSideantal: " + str(self.antalsider))


class Film(Materiale):
    """En child class til Materiale til at beskrive film"""
    def __init__(self, idnr, titel, aarstal, instruktor, lengde:int, antal:int=1):
        super().__init__(idnr, titel, aarstal, antal=antal)
        self.instruktor = instruktor
        self.lengde = lengde

    def toString(self):
        """Udskriver beskrivelse af filmen"""
        print("Titel og årstal: " + self.titel + " (" + str(self.aarstal) + (")") +
              "\nInstruktor: " + self.instruktor +
              "\nid: " + str(self.idnr) +
              "\nAntal kopier: " + str(self.antal) +
              "\nAntal udlånte kopier: " + str(self.antal_udlaan) +
              "\nSpilletid: " + str(self.lengde) + " min.")

