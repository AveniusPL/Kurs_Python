zakres = input("Podaj zakres liczbowy")
zakres = int(zakres)
zakres = range(zakres)
liczby_nie_pierwsze = []

for i in zakres:
    c = i * i
    if c not in zakres:
        print(i, "jest liczbą pierwszą")
        zakres(i)
    if i not in liczby_nie_pierwsze:
        liczby_nie_pierwsze.append(i)
print(liczby_nie_pierwsze)