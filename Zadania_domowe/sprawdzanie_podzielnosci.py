liczba = input("Podaj swoją liczbę")
int_liczba = liczba
if liczba.isdigit():
    # "123" >> TRUE
    # "MARYSIA" >> FALSE

    if liczba % 3 == 0:
        wynik = liczba/3
        print ("Twoja liczba jest podzielna przez 3 i jej wynik to :" + wynik)
    if liczba % 5 == 0:
        wynik = liczba / 5
        print ("Twoja liczba jest podzielna przez 5 i jej wynik to :" + wynik)
    if liczba % 7 == 7 :
        wynik = liczba / 7
        print ("Twoja liczba jest podzielna przez 7 i jej wynik to :" + wynik)
    else:
        print ("Twoja liczba jest nie podzielna")
else:
   print ("Nie wprowadziłeś liczby")