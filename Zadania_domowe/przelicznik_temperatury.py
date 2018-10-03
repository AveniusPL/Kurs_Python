#jeśli w stringu wykrywa na koncu C to ma na F przekształcać a jak F to na C zapomocą SLICE

temperatura = input ("Podaj mi temperaturę : ")
znak = temperatura[-1:]


if znak == "f" or znak == "F":
    temperatura_F = temperatura[:-1]
    temperatura_C = (int(temperatura_F) - 32) * 5 / 9
    temperatura_C = str(temperatura_C)
    print (temperatura_C[0:5]+ "C")
elif znak == "c" or znak == "C":
    temperatura_C = temperatura[:-1]
    temperatura_F = (int(temperatura_C) * (9/5)) + 32
    temperatura_F = str(temperatura_F)
    print (temperatura_F[0:5] + "F")
else:
    print ("Źle wprowadziłeś temperaturę.")