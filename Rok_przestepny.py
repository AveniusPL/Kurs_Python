rok = int( input("Podaj aktualny rok"))

def rok_przestepny():

    global rok
    if (rok % 4 == 0 and rok % 100 !=0) or rok % 400 == 0:
        print("Rok jest przestępny")
    else:
        print("Rok nie jest przetepny")
rok_przestepny()
