"""
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict. 
"""

seasons= ['winter', 'spring', 'summer', 'autumn']
seasons_number = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month == 3 or month == 4 or month ==5:
    print(seasons_number.get(2))
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_number.get(3))
    print(seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_number.get(4))
    print(seasons[3])
elif month ==1 or month == 12 or month == 2:
    print(seasons_number.get(1))
    print(seasons[0])
else: print('ERROR')
