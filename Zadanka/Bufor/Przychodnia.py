# # Przychodnia
# # max dziennie 4 osób jak za duzo to wyjątek
# zliczać pacjentów do lekarza
# Day - doc - pacient
class Human:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def full_name(self):
        return "{} {}".format(imie, nazwisko) 

        )
class Clinic:
    calendar = {}
    @classmethod
    def schedule (cls, name):
        cls.name = name

    @classmethod
    def print_per_day (cls):
        #wyswietl pacjentow per doc
    @@classmethod
    def print_per_doc (cls):
        #wyświetl pacjentów per day
class Doctor(Human):
    pass
class Day:
    def __init__(self,name):
        self.name = name
        self.list = {}
class Patient(Human):
    pass


c = Clinic()
doc = Doctor("x","y")
p1 = Patient("Tomek","Dzierwa")
p2 = Patient("Patryk", "Janusz")
p3 = Patient("Wojtek", "Widła")
p4 = Patient("Michał", "Szczerba")
p5 = Patient("Przemek", "Fior")

