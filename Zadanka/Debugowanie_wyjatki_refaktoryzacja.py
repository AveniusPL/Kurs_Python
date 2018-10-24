"""
Debugging - odnajdowanie i usuwanie błedów w programie
debugowanie za pomocą print()
debugowanie za pomocą debuggera
debugger - program pozwalający zatrzymać program w dowolnym miejscu

pythonowy debugger pdb
import pdb
pdb.set_trace() - ustawianie breakpointa

Rubber duck debugging :  nieformalny sposób debugowania kodu. Metoda polega na tym, że programista, próbując znaleźć
 błędy w kodzie (inspekcja kodu), trzyma w pobliżu gumową kaczuszkę lub inny przedmiot nieożywiony. Linia po linii,
 programista tłumaczy kaczuszce lub innemu obiektowi przewidywane funkcje każdego segmentu kodu – podczas sprawdzania
 powinny wyjść na jaw błędy stworzonej aplikacji.

    WYJĄTKI:
syntax error = błąd w składni polecenia
exception,Error = wyjątki - to inaczej błędy powstałe w trakcie wykonywania programu
np. błąd dzielenia przez zero , brak zdefiniowanej zmiennej odwołanie się do nie istniejąćego inteksu itp.
Wyjątek można samemu wywołać celowo.

używamy bloków try,except, finally
"""
#     try:
#         # kod
#     except typbłędu:
#         #kod wywowały gdy zostanie przechwycony błąd o danycm typoe
#     finally: nieobowiązkowy
#         # kod wywołany zawsze , gdy błędu nie będzie i gdy będzie.
"""
Staramy się wyłapywać konkretne typy wyjątków, np VALUERRROR , NAMERROR zamiast Exception
Bloki except deklarujemy od szczegółu do ogółu.
"""
# l = [1,2,3]
# try:
#     print("przed wyjątkiem")
#     print (l[3])
# except IndexError as error:
#     print(error)
#     print(l[2])
# finally:
#     print("po wyjątku")
"""
raise ValueError("zła wartość") wywołuje ręcznie wyjątek 

REFAKTORYZACJA - Proces poprawiania struktury kodu, bez zmiany jego funkcjonalności. 
"""
