slowo = input("Wpisz swoje słowo")
liczby = 0
znaki = 0
i = 0
while slowo == "":
    print("Nic nie wpisałeś....")
    slowo = input("Wpisz swoje słowo")
else:
    while i < len(slowo):
        print(i,"jest : ",slowo[i])
        if slowo[i].isdigit():
            liczby +=1
        else:
            znaki +=1
        i += 1


print ("Ilość cyfr w tym wyrazie : {} \nIlość słów w tym wyrazie to : {}".format(liczby,znaki))