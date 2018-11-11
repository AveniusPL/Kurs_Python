class Magazyn:
    def __init__(self, product_list):
        self.products = product_list

class Produkt:
    def __init__(self , nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc


class Sklep:
    def __init__(self, mag):
        self.magazyn = mag

    def menu(self):
        nazwa = input('podaj nazwe szukanego produktu: ')
        ilosc = input('podaj ile szuk szukasz tego produktu: ')
        ilosc = int(ilosc)
        prod = None

        for product in self.magazyn.products:
            if product.nazwa == nazwa:
                if ilosc <= product.ilosc:
                    prod = product

            if not prod:
                print('nie ma takiego produktu')

            else:
                print('MENU: ')
                print('1. sprawdz stan na sklepie')
                print('2. proszę o fakturkę')

                num_op = input('Co chcesz zrobic? : ')
                if num_op == '1':
                    print(prod.ilosc)
                elif num_op == '2':
                    nazwa = input('jaki produkt chcesz dodac do koszyka? : ')
                    ilosc = input('jaką ilość produktu chcesz dodac do koszyka? : ')

class Faktura:
    def __init__(self, num_op):
        self.num_op = num_op

    def drukuj_fv(self, ttt):
        self.ttt = ttt

        if self.num_op == '2':
            with open('fv.txt', 'w') as f:
                f.write ('Hello, This is sample content.\n')



magazyn = Magazyn([
    Produkt('karma', 10, 14),
    Produkt('platki', 14, 2),
    Produkt('schabowe', 155, 8),
    Produkt('cycki', 2, 2),
])

#prod = sklep([['karma',10,100],['lego',12,45],['platki',56,300],['schwbowe',45,3000]])
ewa_test = Sklep(magazyn)
ewa_test.menu()
