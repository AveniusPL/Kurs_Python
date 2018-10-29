def eratos(n):
    bufor_2 = []
    bufor_3 = []
    bufor_5 = []
    for candidate in range(2, n):
        for divider in range(2, candidate):
            if candidate % divider == 0:
                print("%2d is not a prime number - divider is %2d" % (candidate, divider))
                if divider == 2:
                    bufor_2 += str(candidate)
                elif divider == 3:
                    bufor_3 += str(candidate)
                elif divider == 5:
                    bufor_5 += str(candidate)
                break
        else:
            print("%2d is prime!" % (candidate))
    print(" Te liczby mają dzielnik 2: {} \n Te liczby mają dzielnik 3: {} \n Te liczby mają dzielnik 5: {}".format(
        bufor_2,
        bufor_3,
        bufor_5))


eratos(10)
