"""lista = ["a","b","a","A"]
unikaty = []
i = 0
for i in lista:
    if i not in unikaty:
        unikaty.append(i)
print(unikaty)"""

sumator = 0
lista = ["a","b","a","A"]
#print (sum(lista)) - jeśli w liście sa liczby

for L in lista:
    sumator += L
print(sumator)
