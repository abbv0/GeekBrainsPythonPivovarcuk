class Clothes():

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)

class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5

class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3

a = Coat(48)
b = Suit(1.6)

print(f'Общая площадь - {a.expense + b.expense}')
