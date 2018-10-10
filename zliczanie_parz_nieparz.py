zakres = range(75)
ilosc_parzysta = 0
ilosc_nieparzysta = 0

for liczba in zakres:
    if liczba % 2 == 0:
        ilosc_parzysta += 1

    else:
        ilosc_nieparzysta += 1


print("Ilość parzystych : " , ilosc_parzysta) # a = "ilość parzystych {}, ilość nieparzystych []".format(iloscparzystych, ilosc_nieparzystych)
print("Ilość nieparzystych : " , ilosc_nieparzysta)
