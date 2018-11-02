class Employee(object):
    def __init__(self,firstname,lastname,stawka):
        self.firstname = firstname
        self.lastname = lastname
        self.stawka = stawka

class HEmployee(Employee):
    def oblicz_wynagrodzenie(self,godziny):
        return self.stawka * godziny

class SEmployee(Employee):
    def oblicz_wynagrodzenie(self, godziny):
        return (godziny / 168) * self.stawka

jan_kowalski = HEmployee("Jan", "Kowalski", 100)
print(jan_kowalski.oblicz_wynagrodzenie(8))