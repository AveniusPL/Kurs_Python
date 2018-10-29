#
# class Parent():
#
#     def __init__(self):
#         print("Parent init")
#
#     def parent(self):
#         print("parent parent")
#     def poke(self):
#         print("parent poked")
#
# class Child(Parent):
#
#     def __init__(self):
#         super().__init__()   # Funkcja Super zagląda do rodzica
#         print("Child init")
#
#     def poke(self):
#         print("Child poked")
#
# child = Child()
# child.poke()
# child.parent()
#
# # parent = Parent()
# # parent.parent()
# # parent.poke()


class Person():

    def __init__(self, name):
        self.name = name
        self.surname = "Kwiatkowski"
        self.age = 25

class Employee(Person):

    def __init__(self, position):
        super().__init__("Tomek")
        self.position = position
        self.specialization = "Python"

class Client(Person):

    def __init__(self,name):
        super().__init__(name)
        self.ordered = "Website"

pracownik = Employee("Programmer")
print(pracownik.name)
print(pracownik.position)

pracownik2 = Employee("Designer")
print(pracownik2.name)
print(pracownik2.position)

klient = Client("Marta")
print(klient.name)
print(klient.ordered)

klient2 = Client("Kamila")
print(klient2.name)
print(klient2.ordered)