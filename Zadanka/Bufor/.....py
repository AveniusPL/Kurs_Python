class Person:
   def __init__(self, fn, ln):
       self.__fn = fn
       self.__ln = ln

   @property
   def fn(self):
       return self.__fn

   @fn.setter
   def fn(self, val):
       print("Hej ktos probuje zaktualizowac ln")
       self._fn = val

   @ln.deleter
   def fn(self):
       print('deleter')
       self._fn = ""

   @property
   def ln(self):
       return self.__ln

   @ln.setter
   def ln(self, val):
       print("Hej ktos probuje zaktualizowac ln")
       self._ln = val

   @ln.deleter
   def ln(self):
       print('deleter')
       self._ln = ""

   @property
   def full_name(self):
        if self.ln != None:
            return f"{self.fn} {self.ln}"
        else:
            print("Błąd")

p = Person("Jan", "Kowalski")
print(p.ln)
del p.ln
print(p.ln)
print(p.full_name)