from samochod import Samochod
from silniki import Silniki

silnik = Silniki(300, 1.5)
samochod_1 = Samochod ("Honda", "Civic","Szary",silnik)

silnik = Silniki(140, 1.6)
samochod_2 = Samochod ("Seat", "Ibiza", "Czerwony",silnik)

silnik = Silniki(350, 2.5)
samochod_3 = Samochod ("BMW", "E36", "Czarny",silnik)

def ktory_szybszy(s1 ,s2):
    if s1.silnik.moc > s2.silnik.moc:
        return s1
    else:
        return s2
zwyciezca = ktory_szybszy(samochod_1,samochod_2)
print(zwyciezca.marka, zwyciezca.model)