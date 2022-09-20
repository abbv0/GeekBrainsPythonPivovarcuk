"""
Реализовать класс Matrix (матрица). Обеспечить
перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков)
для формирования матрицы.Далее реализовать
перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[10, 1, 16],
                    [14, 11, 16],
                    [13, 27, 35]],
                   [[23, 23, 29],
                    [17, 41, 14],
                    [19, 53, 7]])

print(my_matrix.__add__())
