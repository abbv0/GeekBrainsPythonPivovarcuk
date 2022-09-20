"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в час'))
        bonus = int(input('Премия '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника {res}')
    except ValueError:
        return print('Not a number')
sal()


# from sys import argv
#
# name, time, salary, bonus = argv
# try:
#     time = int(time)
#     salary = int(salary)
#     bonus = int(bonus)
#     res = time * salary + bonus
#     print(f'заработная плата сотрудника {res}')
# except ValueError:
#     print('VaLuE eRrOr')
