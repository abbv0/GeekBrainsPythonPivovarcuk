"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

my_list = [300, 3, 2, 22, 17, 185, 44, 130]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num] and num != 0]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
