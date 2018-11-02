class Kwiaciarka:
    def __init__(self):
        self.bukiet = []
    def zrobbukiet(self, kwiaty):
        pass

    def wystawrachunek(self,zamowienie):
        return
class Kwiat:
    def __init__(self,cena,nazwa):
        self.cena = cena
        self.nazwa = nazwa

class Bukiet(Kwiaciarka):

    def zbior(self, kwiat):
        return self.bukiet.append(kwiat)


