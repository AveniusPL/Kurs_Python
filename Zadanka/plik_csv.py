"""
pliki CSV - comma separated vales - dane oddzielane przecinkami

Imię,nazwisko,adres,telefon

do obsługi plików CSV można użyć biblioteki CSV

Otwieranie modułu csv:
    import csv
    kontekst manager do otwierania pliku
    delimeter = " " - oddziela postrzegulne kolumny
    iterable - kolekcja typów danych możliwych do literowania (stringi, liczby, listy)
"""
import csv
with open("baza.csv", 'r') as f:
    reader_object = csv.reader(f, delimiter=";")
    print("Nagłówek")
    print(next(reader_object))
    print("Dane")
    for row in reader_object:
        print(row)

with open('baza.csv', "a", newline="") as f:
    writer_object = csv.writer(f, delimiter= ";")
    writer_object.writerow(["Marian", "Nowak", "Kapelanka 12", "213213123"])