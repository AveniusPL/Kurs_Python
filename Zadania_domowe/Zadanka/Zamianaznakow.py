print("\nWitaj w programie do operacji na łancuchach znaków\n")
def wstep():
    global zdanie
    zdanie = input("Podaj swoje zdanie : ")

def menu():
    print ( "MENU : ")
    print (" 1 - Zamienić litery na duże.")
    print (" 2 - Zammień litery na małe")
    print (" 3 - Zamień wybrane znaki w zdaniu na inne\n")

def zamiana_duze():
    global zdanie
    zdanie = zdanie.upper()
    print ("Twoje zdanie : " + zdanie)
    return

def zamiana_male():
    global zdanie
    zdanie = zdanie.lower()
    print ("Twoje zdanie : " + zdanie)
    return

def zamiana_znaku():
    global zdanie
    znak = input("podaj znak do zamiany : ")
    zamiana = input("podaj znak zamieniajacy : ")
    zdanie = zdanie.replace (znak, zamiana )
    print (zdanie)
    return
wstep()
menu()
operacja = input("Co wybierasz? : ")
while operacja != "0":
    if operacja=="1": zamiana_duze()
    elif operacja=="2": zamiana_male()
    elif operacja=="3": zamiana_znaku()
    else: print("Wpisałeś niewłaściwą liczbę")
    wstep()
    menu()
    operacja = input("Co wybierzesz ? ")