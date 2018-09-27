from math import sqrt
print("Witaj w programie, którego zadaniem jest obliczanie pola oraz obwodu podstawowych figur geometczynych")

def menu():
    print (""" """)
    print ("""..::::::::::::::::::::.. || MENU || ..::::::::::::::::::::..""")
    print ("Wybierz swoją figurę w celu obliczeń pola oraz jej obwodu. Wymiary podawaj w centymentrach.")
    print ("..:: 1 - prostokąt          ::..")
    print ("..:: 2 - kwadrat            ::..")
    print ("..:: 3 - równoległobok      ::..")
    print ("..:: 4 - romb               ::..")
    print ("..:: 5 - trójkąt            ::..")
    print ("..:: 6 - trójkąt prostokątny::..")
    print ("..:: 7 - trapez             ::..")
    print ("..:: 8 - trapez prostokątny ::..")
    print ("..:: 9 - koniec             ::..")
    print ("..:: 0 - MENU               ::..")
    print (""" """)

def prostokąt():
    print("Wybrałeś prostokąt. Proszę podaj mi wymiary a i b")
    a = input("Wymiar krótszej ściany : ")
    a = int(a)
    b = input("Wymiar dłuższej ściany : ")
    b = int(b)
    pole = sqrt(a)
    pole = str(pole)
    obwod = a + a + b + b
    obwod = str(obwod)
    print ("")
    print ("Pole prostokąta to: " + pole + "cm." )
    print ("Obwód prostokąta to: " + obwod + "cm.\n")
    return

def kwadrat():
    print("Wybrałeś kwadrat. Proszę podaj mi wymiar a")
    a = input("Wymiar boku a : ")
    a = int(a)
    pole = a * a
    pole = str(pole)
    obwod = a + a + a + a
    obwod = str(obwod)
    print("")
    print("Pole kwadratu to: " + pole + "cm.")
    print("Obwód kwadratu to: " + obwod + "cm.\n")
    return

def rownoleglobok():
    print("Wybrałeś równoległobok. Proszę podaj mi wymiary a, b oraz h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    b = input("Wymiar ściany b : ")
    b = int(b)
    h = input("Wymiar wysokości h :")
    h = int(h)
    pole = a * h
    pole = str(pole)
    obwod = a + a + b + b
    obwod = str(obwod)
    print ("")
    print ("Pole równoległoboku to: " + pole + "cm." )
    print ("Obwód równoległoboku to: " + obwod + "cm.\n")
    return

def romb():
    print("Wybrałeś romb. Proszę podaj mi wymiary a i h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    h = input("Wymiar wysokości h : ")
    h = int(b)
    pole = a * h
    pole = str(pole)
    obwod = a + a + a + a
    obwod = str(obwod)
    print ("")
    print ("Pole rombu to: " + pole + "cm." )
    print ("Obwód rombu to: " + obwod + "cm.\n")
    return

def trojkat():
    print("Wybrałeś trójkąt. Proszę podaj mi wymiary a, b, c oraz h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    b = input("Wymiar ściany b : ")
    b = int(b)
    c = input("Wymiar ściany c : ")
    c = int(c)
    h = input("Wymiar wysokości h : ")
    h = int(h)
    pole = a * h / 2
    pole = str(pole)
    obwod = a + b + c
    obwod = str(obwod)
    print ("")
    print ("Pole trójkąta to: " + pole + "cm." )
    print ("Obwód trójkąta to: " + obwod + "cm.\n")
    return

def trojkatprostokatny():
    print("Wybrałeś trójkąt prostokątny. Proszę podaj mi wymiary a, b, c oraz h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    b = input("Wymiar ściany b : ")
    b = int(b)
    c = input("Wymiar ściany c : ")
    c = int(c)
    pole = ( a * b ) / 2
    pole = str(pole)
    obwod = a + b + c
    obwod = str(obwod)
    print ("")
    print ("Pole trójkąta prostokątnego to: " + pole + "cm." )
    print ("Obwód trójkąta prostokątnego to: " + obwod + "cm.\n")
    return

def trapez():
    print("Wybrałeś trapez. Proszę podaj mi wymiary a, b, c, d oraz h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    b = input("Wymiar ściany b : ")
    b = int(b)
    c = input("Wymiar ściany c : ")
    c = int(c)
    d = input("Wymiar ściany d : ")
    d = int(d)
    h = input("Wymiar wysokośći h : ")
    h = int(h)
    pole = (( a + b ) * h) / 2
    pole = str(pole)
    obwod = a + b + c + d
    obwod = str(obwod)
    print ("")
    print ("Pole trapeza to: " + pole + "cm." )
    print ("Obwód trapeza to: " + obwod + "cm.\n")
    return

def trapezprostokatny():
    print("Wybrałeś trapez prostokątny. Proszę podaj mi wymiary a, b, c oraz h")
    a = input("Wymiar ściany a : ")
    a = int(a)
    b = input("Wymiar ściany b : ")
    b = int(b)
    c = input("Wymiar ściany c : ")
    c = int(c)
    h = input("Wymiar wysokośći h : ")
    h = int(h)
    pole = (( a + b ) * h) / 2
    pole = str(pole)
    obwod = a + b + c + h
    obwod = str(obwod)
    print ("")
    print ("Pole trapeza prostokątnego to: " + pole + "cm." )
    print ("Obwód trapeza prostokątnego to: " + obwod + "cm.\n")
    return

menu()
operacja = input("Co wybierasz? ")
while operacja != "0":
    if operacja=="1": print (":::wybrałeś prostokąt:::\n"),prostokąt()
    elif operacja=="2": print (":::wybrałeś kwadrat:::\n"),kwadrat()
    elif operacja=="3": print (":::równoległobok:::\n"),rownoleglobok()
    elif operacja=="4": print (":::romb:::\n"),romb()
    elif operacja=="5": print (":::trójkąt:::\n"),trojkat()
    elif operacja=="6": print (":::trójkąt prostokątny:::\n"), trojkatprostokatny()
    elif operacja=="7": print (":::trapez:::\n"),trapez()
    elif operacja=="8": print(":::trapez prostokątny:::\n"), trapezprostokatny()
    elif operacja=="9": break
    elif operacja=="0": menu()
    else: print("Wpisałeś niewłaściwą liczbę")
    operacja = input("Co wybierzesz ? ")