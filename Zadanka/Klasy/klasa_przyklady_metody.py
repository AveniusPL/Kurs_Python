# class Foo(object):
#     def __init__(self):
#         pass
#     def __del__(self):
#         pass
# f = Foo()

class Complex(object):
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(
        self.real + other.real,
        self.img + other.img)

    def __sub__(self, other):
        return Complex(
        self.real - other.real,
        self.img - other.img)

    def __mul__(self, other):
        return Complex(
            (self.real*other.real)-(self.img*other.img),
            (self.real*other.img)+(self.img*other.real))
        pass
    def __pow__(self, power, modulo=None):
        if power == 2:
            return self * self
a = Complex(1,2)
b = Complex(3,4)
c = a ** 2
print("{} + {}i".format(c.real,c.img))

class Fib:
    def __init__(self,n):
        self.a = 0
        self.b = 1
        self.max = n

    def __iter__(self):
        return self
    def __next__(self):
        t = self.a
        self.a = self.b
        self.b +=t
        return self.a
    raise StopIteration()


for i in Fib(10):
    print(i)

