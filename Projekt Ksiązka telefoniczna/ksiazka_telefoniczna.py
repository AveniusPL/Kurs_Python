# DANE DO PROGRAMU :
lista_kontaktow = [["Patryk","Janusz",792008840],["Tomasz","Wolny",792009940]]
print("Witaj w programie KSIĄZKA TELEFONICZNA.")

def menu():
    print (" ")
    print ("..::::::::::::::::::::.. || MENU || ..::::::::::::::::::::..")
    print ("Wybierz co planujesz zrobić : ")
    print ("")
    print ("..:: 1 - wyszukiwanie kontaktu         ::..")
    print ("..:: 2 - dodawanie kontaktu            ::..")
    print ("..:: 3 - usuwanie kontaktu             ::..")
    print ("..:: 4 - edytowanie danych w kontakcie ::..")
    print ("..:: 5 - wyczyść listę kontaktów       ::..")
    print ("..:: 6 - koniec                        ::..")
    print (" ")

def menu_wyszukiwanie():
    wyjscie = True
    print("|xЖx| 1 - wyszukiwanie po imieniu          |xЖx|")
    print("|xЖx| 2 - wyszukiwanie po nazwisku         |xЖx|")
    print("|xЖx| 3 - wyszukiwanie po numerze telefonu |xЖx|")
    print("|xЖx| 4 - wróć                             |xЖx|")
    operacja = input("Co wybierasz? ")
    while operacja != "0" and wyjscie:
        if operacja == "1":
            print(":::wybrałeś wyszukiwanie po imieniu:::\n")
            local_imie = input("Wpisz imię: ").capitalize()
            for i in lista_kontaktow :
                if i[0] == local_imie :
                    print("Oto twój kontakt :", i)


        elif operacja == "2":
            print(":::wybrałeś wyszukiwanie po nazwisku:::\n")
            local_nazwisko = input("Wpisz nazwisko: ").capitalize()
            for i in lista_kontaktow:
                if i[1] == local_nazwisko:
                    print("Oto twój kontakt :", i)
                    wyjscie = False
                    break
                if wyjscie == False:
                    print("Nie znaleziono w liście kontaktów")
                wyjscie = False
        elif operacja == "3":
            print(":::wybrałeś wyszukiwanie po numerze telefonu:::\n")
            local_telefon = int(input("Wpisz numer telefonu: "))
            for i in lista_kontaktow:
                if i[2] == local_telefon:
                    print("Oto twój kontakt :", i)
                    wyjscie = False
                    break
                if wyjscie == False:
                    print("Nie znaleziono w liście kontaktów")
                wyjscie = False
        elif operacja == "4":
            print(":::wybrałeś powrót do wcześniejszego menu:::\n")
            wyjscie = False
        else:
            print("Wpisałeś niewłaściwą liczbę")

def dodawanie_kontaktu():
    local_kontakt = []
    local_imie = input("Wpisz imię: ")
    local_nazwisko = input("Wpisz nazwisko: ")
    local_telefon = input("Wpisz numer telefonu: ")
    local_kontakt.append(local_imie.capitalize())
    local_kontakt.append(local_nazwisko.capitalize())
    local_kontakt.append(int(local_telefon))

    if local_kontakt not in lista_kontaktow:
        lista_kontaktow.append(local_kontakt)
        print("Twój kontakt został dodany do listy kontaktów.")
        print(lista_kontaktow)
    else:
        print("Ten kontakt znajduję się już na liście kontaktów."), dodawanie_kontaktu()
def usuwanie_kontaktu():
    wyjscie = True
    print("|xЖx| Wyszukaj kontakt, który chcesz usunąć|xЖx|")
    print("|xЖx| 1 - wyszukiwanie po imieniu          |xЖx|")
    print("|xЖx| 2 - wyszukiwanie po nazwisku         |xЖx|")
    print("|xЖx| 3 - wyszukiwanie po numerze telefonu |xЖx|")
    print("|xЖx| 4 - wróć                             |xЖx|")
    operacja = input("Co wybierasz? ")
    while operacja != "0" and wyjscie:
        if operacja == "1":
            print(":::wybrałeś wyszukiwanie po imieniu:::\n")
            local_imie = input("Wpisz imię: ").capitalize()
            for i in lista_kontaktow:
                if i[0] == local_imie:
                    print ("Twój kontakt :",i,"został usunięty.")
                    lista_kontaktow.remove(i)
                    wyjscie = False
                    break
                if wyjscie == False:
                    print("Nie znaleziono w liście kontaktów")
                wyjscie = False
        elif operacja == "2":
            print(":::wybrałeś wyszukiwanie po nazwisku:::\n")
            local_nazwisko = input("Wpisz nazwisko: ").capitalize()
            for i in lista_kontaktow:
                if i[1] == local_nazwisko:
                    print("Oto twój kontakt :", i)
                    wyjscie = False
                    break
                if wyjscie == False:
                    print("Nie znaleziono w liście kontaktów")
                wyjscie = False
        elif operacja == "3":
            print(":::wybrałeś wyszukiwanie po numerze telefonu:::\n")
            local_telefon = int(input("Wpisz numer telefonu: "))
            for i in lista_kontaktow:
                if i[2] == local_telefon:
                    print("Oto twój kontakt :", i)
                    wyjscie = False
                    break
                if wyjscie == False:
                    print("Nie znaleziono w liście kontaktów")
                wyjscie = False
        elif operacja == "4":
            print(":::wybrałeś powrót do wcześniejszego menu:::\n")
            wyjscie = False
        else:
            print("Wpisałeś niewłaściwą liczbę")

def menu_edytowanie():
    print("|xЖx| 1 - edytowanie imienia          |xЖx|")
    print("|xЖx| 2 - edytowanie nazwiska         |xЖx|")
    print("|xЖx| 3 - edytowanie numeru telefonu  |xЖx|")
    print("|xЖx| 4 - wróć                        |xЖx|")
    operacja = input("Co wybierasz? ")
    while operacja != "0":
        if operacja == "1":
            print(":::wybrałeś edytowanie po imieniu:::\n"),  # menu_wyszukiwanie()
        elif operacja == "2":
            print(":::wybrałeś edytowanie po nazwisku:::\n"),  # dodawanie_kontaktu()
        elif operacja == "3":
            print(":::wybrałeś edytowanie po numerze telefonu:::\n"),  # usuwanie_kontaktu()
        elif operacja == "4":
            print(":::wybrałeś powrót do wcześniejszego menu:::\n"),  # menu_edytowanie()

def reset_listy():
    odpowiedz = input("Czy na pewno chcesz usunąć listę kontaktów? Wpisz TAK lub NIE : ")
    if odpowiedz == "tak" or odpowiedz == "Tak" or odpowiedz == "TAK":
        lista_kontaktow.clear()
        print("Twoja lista została wyczyszczona.")
    else:
        print("Coś źle wpisałeś. ")

menu()
operacja = input("Co wybierasz? ")
while operacja != "0":
    if operacja=="1": print ("::: wybrałeś opcję wyszukiwania kontaktu :::\n"),menu_wyszukiwanie()
    elif operacja=="2": print ("::: wybrałeś dodawanie nowego kontaktu:::\n"),dodawanie_kontaktu()
    elif operacja=="3": print ("::: wybrałeś usuwanie kontaktu:::\n"), usuwanie_kontaktu()
    elif operacja=="4": print ("::: wybrałeś edytowanie kontaktu:::\n"),menu_edytowanie()
    elif operacja=="5": print (":::wybrałeś wyczyszczenie listy kontaków:::\n"),reset_listy()
    elif operacja=="6": break
    else: print("Wpisałeś niewłaściwą liczbę")
    operacja = input("Co wybierzesz ? ")