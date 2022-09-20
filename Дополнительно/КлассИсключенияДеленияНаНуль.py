"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в 
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class Сlass_exception:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Нельзя делить на ноль")


div = Сlass_exception(6, 26)
print(Сlass_exception.divide_by_null(26, 6))
print(Сlass_exception.divide_by_null(26, 0))
print(div.divide_by_null(0, 26))
