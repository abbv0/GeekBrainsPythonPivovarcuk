"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). 
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

"""

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(int(self.quantity - other.quantity)) if (self.quantity - other.quantity) > 0 else print('Результат операции Отрицательное значение')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity)) if (self.quantity - other.quantity) > 0 else print('Результат операции Нехорошее деление')

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(4)
cells2 = Cell(8)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(15))
print(cells1.make_order(5))
print(cells1 / cells2)
