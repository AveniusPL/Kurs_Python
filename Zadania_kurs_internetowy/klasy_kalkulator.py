class Calculator():

    def __init__(self):
        print("Jesteśmy w klasie")

    def __del__(self):
        print("Wyszliśmy z klasy")

    def __str__(self):
        return "Hello"

    def __int__(self):
        return 10

    def __len__(self):
        return 5

    def __bool__(self):
        return True
    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)


# def main():
#     print("1")
#     calc = Calculator()
#     print("2")
#     calc.dodaj( 10, 10)
#     print("3")
#
# main()
# print("4")

calc = Calculator()

calc.dodaj(10,10)
print(calc)

wynik = int(calc) + 50
print(wynik)

print(len(calc))

if calc:
    print("True")
else:
    print("False")