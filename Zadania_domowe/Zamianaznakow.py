zdanie = input("Podaj swoje zdanie : ")

def menu():
    print (" 1 - Zamienić litery na duże.")
    print (" 2 - Zammień litery na małe")
    print (" 3 - Zamień wybrane znaki w zdaniu na inne")

def zamiana_duze():
    zdanie.upper()
    print ("O to Twoje zdanie : " + zdanie)
    return

def zamiana_male():
    znak_dozamiany = input("Wpisz znak jaki chcesz zamienić")
    podmieniajacy = input("Wpisz znak na który chcesz zamienić")
    return

def zamiana_inne():
    znak_dozamiany = input("Wpisz znak jaki chcesz zamienić")
    podmieniajacy = input("Wpisz znak na który chcesz zamienić")
    return


menu()
operacja = input("Co wybierasz? ")
while operacja != "0":
    if operacja=="1": zamiana_duze()
    elif operacja=="2": zamiana_male()
    elif operacja=="3": zamiana_inne()
    else: print("Wpisałeś niewłaściwą liczbę")
