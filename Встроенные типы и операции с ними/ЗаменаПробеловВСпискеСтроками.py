"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
"""

slova = input('Введите слова через пробел')
print()
slovo = []
number = 1
for element in range(slova.count(' ') + 1):
    slovo = slova.split()
    if len(str(slovo)) <= 10:
        print(f" {number} {slovo [element]}")
        number += 1
    else:
        print(f" {number} {slovo [element] [0:10]}")
        number += 1
