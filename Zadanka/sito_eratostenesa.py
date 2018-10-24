def eratos(n):
    wykreslenia = []
    for liczba in range (2,n+1):
        if liczba not in wykreslenia:
            print(liczba)
        for wykreslone in range (liczba+liczba,n,liczba):
            wykreslenia.append(wykreslone)
            print(wykreslenia)
eratos(10)












    # print(" Te liczby mają dzielnik 2: {} \n Te liczby mają dzielnik 3: {} \n Te liczby mają dzielnik 5: {}".format(
    #     bufor_2,
    #     bufor_3,
    #     bufor_5))