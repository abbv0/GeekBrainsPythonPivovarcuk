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