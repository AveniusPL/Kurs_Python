class Calculator():

    def __init__(self):
        print("Jesteśmy w klasie")
        self.liczba = 10
        self.ostatni_wynik = 0
    def __del__(self):
        print("Wyszliśmy z klasy")

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik)

calc = Calculator()
calc.dodaj(5,3)
calc.dodaj(10,10)
calc.odejmij(10,5)

calc2 = Calculator()
calc2.dodaj(50,50)
calc2.dodaj(150,15)
print("Ostatni wynik calc : {}".format(calc.ostatni_wynik))
print("Ostatni wynik calc2: {}".format(calc2.ostatni_wynik))

# calc.liczba
# print("calc --",calc.liczba)
# calc.liczba += 10
# print("calc + 10 = ",calc.liczba)
#
# calc2 = Calculator()
# print("calc2 -- ",calc2.liczba)
# print("calc -- " ,calc.liczba)