"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = int(input('Введите число n '))
nn = int('{}{}'.format(n,n))
nnn = int('{}{}{}'.format(n,n,n))
itog = n + nn + nnn
print(itog)
