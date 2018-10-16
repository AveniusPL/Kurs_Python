"""dodawanie()
        odejmowanie()
        odejmowanie ()
        menu = [dod,odej,edy]
        aktyw_fn = menu[0]
        aktywn_fn()"""

"""def foo(imie,nazwisko):
                    return f"{imie} {nazwisko}"
                napis = foo ("Jan","Tomek")
                print(napis)"""

"""def dodaj_imie(imie, imiona=[]):
    imiona.append(imie)
    return imiona                       #Zmienne domyśle są deklarowane tylko raz i to na początku uruchomienia programu.
print(dodaj_imie("Tomek"))              #Zaleca się używania typów prymitywnych nie mutowalnych.
print(dodaj_imie("Monika"))
print(dodaj_imie("Kamil"))"""
"""imie = "Ania"

def foo():
    imie = "Jola"
    print("wenatrz", imie)     # na typyzłożone nie trzeba definiować ich jako global

foo()
print(imie)
"""
"""lista = ["a","b","a","A"]

def sumator(lis):
    sum = 0
    for i in lis:
        sum += 1
    return sum

x = sumator()
print(x)"""


"""def palidrom(slowo="oko"):
   if slowo[:] == slowo[::-1]:
     return "tak"
   else:
       return "nie jest"
zdanie = sprawdzanie()
print(zdanie)
"""
def isPalindrome(s):
    return s == s[::-1]
print(isPalindrome("oko"))

def isPalindrome(s):
    lewy_i = 0
    prawy_i = len(s) - 1
    while lewy_i >= prawy_i:
        if s[lewy_i] != s[prawy_i]:
            return False
        lewy_i +=1
        prawy_i -=1
    return  True

"""zakres = range(100)
lista_dzielniki = 0
#sumator wykorzystujemy
for i in zakres:
    if i % 

#zadanie: trójkąt pascala , odwrotna notacja polska """