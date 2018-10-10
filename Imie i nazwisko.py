
print ("Hej, podasz mi swoje imię i nazwisko?");
odpowiedz = input ("wpisz swoją odpowiedz : ");
if  odpowiedz == "tak" or "Tak" or "ok" or "Ok":
    imie = input("Wpisz tutaj swoje imię: ");
    nazwisko = input("Wpisz tutaj swoje nazwisko: ");
    print ("Cześć "+ imie +" " + nazwisko + ". Co u Ciebie słychać");
else:
    print ("Ale z Ciebie małpa :) ");