liczba = 0

for i in range(100):
    liczba += 1
    if liczba % 3 == 0:
            print(liczba, "Fizz ")
    elif liczba % 5 == 0:
            print(liczba, "Buzz")
    elif liczba % 3 == 0 and liczba % 5 == 0:
            print(liczba, "FizzBuzz ")
    else:
        print(liczba)