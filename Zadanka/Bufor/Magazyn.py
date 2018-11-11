class Magazyn(object):
    def __init__(self, products_dict):
        self.products = products_dict

class Produkt(object):
    def __init__(self ,nazwa,cena,ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc


class Sklep(object):
    def __init__(self, prod):
        self.prod = prod
        self.local = []
        # self.koszyk = []
        self.ilosc = None
        self.nazwa = None
    def menu(self):
        self.prod = prod
        # self.koszyk = []
        self.nazwa = None
        self.nazwa = input('podaj nazwe szukanego produktu: ')

        for produkt in self.prod.products:
            if produkt == self.nazwa:
                self.ilosc = input('podaj ile sztuk szukasz tego produktu: ')

                if int(self.prod.products[self.nazwa].ilosc) - int(self.ilosc) > 0:
                    self.local = self.prod.products[self.nazwa]

        if not self.local :
            print("Nie ma takiego produktu lub nie ma tylu sztuk na stanie")


        else:
            print('MENU: ')
            print('1. sprawdz stan na sklepie')
            print('2. dodaj do koszyka ')
            print('3. wyjdz')

            num_op = input('Co chcesz zrobic? : ')
            x = True
            while x:
                if num_op == "1":
                    print(self.local.ilosc)
                    break
                if num_op == "2":
                    print("zawartość koszyka to: Produkt {},"
                          " ilość {} oraz cena {}zł".format(self.nazwa,self.ilosc,self.prod.products[self.nazwa].cena))
                    koszyk = "Produkt:"+ self.nazwa,\
                             "Ilość:" + str(self.ilosc) ,\
                             "Cena:" + str(self.prod.products[self.nazwa].cena)
                    num_op2 = input("Jeśli chcesz dobrać kolejny produkt wpisz TAK "
                                    "lub dla wydrukowania faktury wpisz NIE : ")
                    if num_op2 == "TAK" or num_op2 == "tak":
                        continue
                    elif num_op2 == "NIE" or num_op2 == "tak":
                        with open('fv.txt', 'w', encoding="utf-8") as f:
                            f.write(str(koszyk))
                            print("Faktura wydrukowana")
                            break

                if num_op == "3":
                    break


prod = Magazyn({
    "karma" : Produkt("karma",10,100),
    "platki": Produkt("platki", 56, 300),
    "schabowe": Produkt("schabowe", 45, 3000)})
print(prod.products)
test = Sklep(prod)
test.menu()

