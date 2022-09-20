"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой.
"""

def my_func(name, familiya, year, city, email, telephone):
    return ' '.join([name, familiya, year, city, email, telephone])

print(my_func(name='Andrey',
              familiya='Pivovarchuk',
              year='1000',
              city='Moscow',
              email='nevazhno@gmail.com',
              telephone='8-800-555-35-35'))
