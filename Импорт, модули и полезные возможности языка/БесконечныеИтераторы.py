"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
"""

# -----------------------a-----------------------
from itertools import count
import sys

for el in count(int(input('Введите стартовое число '))):
   print(el)
   if el > 9999:
       print('Цифра 10000 достигнута')
       sys.exit()

# -----------------------b-----------------------
from itertools import cycle, count
import sys

i=0
my_list = ['abcdfg', 'False', False, 191258, None]

for el in cycle(my_list):
    print(el)
    i=i+1
    if i == 10000:
        print('Цикл сработал 10 000 раз')
        sys.exit()
