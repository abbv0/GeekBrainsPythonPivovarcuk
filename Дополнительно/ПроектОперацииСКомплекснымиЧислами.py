class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма - ')
        return f'summ = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение - ')
        return f'multiplication = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


a = ComplexNumber(1, -2)
b = ComplexNumber(3, 4)
print(a)
print(b)
print('')
print(a + b)
print('')
print(a * b)
