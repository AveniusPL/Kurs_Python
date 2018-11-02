"""
Wszystko w python jest obiektem.

Dane ww. sa instancjami obiektu, każdy obiekt ma :
- typ
- wewnętrzą reprezantację danych (prostam złożona)
- zestaw procedur do interakcji z obiektem

Każda instancja jest konkretnym typem obiektu:
- 1234 jest instancją INT
- x = "Natalia" = x jest istancją STRING

INSTANCJA - pojedyncze wystąpienie niezależnego kodu zgodnego z danym wzorcem
Klasa vs instancja :

KLASA - jest "Ideą", "schematem","wyobrażeniem"
Instancja - jest " powołanym do życia" obiektem, który zawiera określone przez klasę właściwości.
można mieć kilka instancji jednej klasy.

Do stworzenia klasy potrzebujemy :
- nazwy klasy
- zdefiniowwać właściwośći klasy

używanie klasy polega na:
- utworzeniu nowej instancji obiektu
- wykonywanie operacji na instancji

def accelereate(self, value):
    self.speed += value

zalety OOP:
    -tworzenie jednorodnego pakietu, zawierającego dane oraz sposoby manipulowania nimi
    -umożliwiają podejście - divide and concquer ( dziel i zwyciężaj)
        - można testować zachowanie kazdej z klas oddzielnie
        - zwieksza modularność, zmniejsza kompleksowość
    -klasy ułatwiają ponowne użycie kodu
        = każda z klas tworzy oddzielnie "środowissko" - różne klasy mogą mieć takie same nazwy funkcji
        - dziedziczenie pozwala aby podklasa, zredefiniowała lub rozszerzyła wybrane właściwości klasy nadrzędnej

    class Complex (object):
        def __init__ (self, real, imag)
        self.real = real
        self.imag = imaginary


        Paradygmaty OOP :
        - ABSTRAKCJA :
        - DZIEDZICZENIE:
             Pozwala na dziedziczenie metod oraz atrybutów z klasy rodzica.
        - ENKAPSULACJA
"           Enkapsulacja inaczej zwana hermetyzacją (kapsułkowaniem) jest to jedno z głównych założeń programowania
            obiektowego. Polega na ukrywaniu metod i atrybutów dla klas zewnętrznych. Dostęp do nich możliwy jest tylko z wewnątrz
             klasy, do której należą, z klas zaprzyjaźnionych lub z klas dziedziczących.
        - POLIMORFIZM(DUCK DUCK TYPING):
        Objekty mogą być użyte w pętli for


        isinstance(obiekt,klasa) - sprzawdza czy dany obiekt jest instancją klasy

    issubclass(klasaA, klasaB)-sprzawdza czy klasaA jest podklasą klasy B


class Samochod(object):
    def __init__(self,user_model="Honda"):
        # print("I am in init !!!")
        self.model = user_model
        self.predkosc = 0
    def zatrab(self):
        print("Honk Honk")

    def przyspiesz(self,wartosc):
        self.predkosc += wartosc

samochod1 = Samochod("VW")
samochod1.zatrab()
samochod1.przyspiesz(10)
print(samochod1.predkosc)
samochod1.przyspiesz(10)
print(samochod1.predkosc)
print(samochod1.model)


# samochod2 = Sampchod()
# print(samochod2.model)
