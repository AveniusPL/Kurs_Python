
#Zadanie 1
imie = input("Podaj swoje imię : ")
def sprawdzanie():
    global imie
    if imie.endswith("a"):
        print ("To jest imię damskie.")
    else:
        print("To jest imie męskie.")
sprawdzanie()



