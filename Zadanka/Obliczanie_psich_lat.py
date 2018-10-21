wiek = input("Podaj wiek swojego psa to oblicze go na ludzkie : ")
wiek_ludzki = 0
i = 0
c = 0
while wiek == "":
    print("Nic nie wpisałeś....")
    wiek = input("Wpisz wiek psa.")
else:
   while i < int(wiek):
        while i < 2:
            i += 1
            wiek_ludzki += 10.5
        else:
            i += 1
            wiek_ludzki += 4
print(wiek_ludzki)