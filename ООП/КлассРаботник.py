"""
Реализовать базовый класс Worker (работник).
 
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

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

my_position = Position ('director', 'Andrey', 'Pivovarchuk', 100, 500)
my_position.get_full_name()
my_position.get_total_income()
