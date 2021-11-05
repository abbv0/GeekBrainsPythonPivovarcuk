class Worker:
    def __init__(self, position, name, surname, wage, bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, position, name, surname, wage, bonus):
        super().__init__(position, name, surname, wage, bonus)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

my_position = Position ('director', 'Andrey', 'Pivovarcuk', 100, 500)
my_position.get_full_name()
my_position.get_total_income()