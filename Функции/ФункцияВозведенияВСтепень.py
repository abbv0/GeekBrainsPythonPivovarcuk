"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

import sys

def proverka_na_deistvitelnoye_i_polozitelnoye(chislo_na_proverku):
    if chislo_na_proverku.isdigit() == False:
        sys.exit(f'{chislo_na_proverku} это нехороший ввод, по условию нужно действительное положительное число')
    else:
        print(f'{chislo_na_proverku} это хорошее число')
        return chislo_na_proverku

def proverka_na_celoe_i_otricatelnoe(chislo_na_proverku):
    try:
        chislo_na_proverku=int(chislo_na_proverku)
        if chislo_na_proverku < 0:
            print(f'{chislo_na_proverku} это хорошее число')
            return chislo_na_proverku
        else:
            sys.exit(f'{chislo_na_proverku} это нехороший ввод, по условию нужно целое отрицательное число')
    except ValueError:
        sys.exit(f'{chislo_na_proverku} это нехороший ввод, по условию нужно целое отрицательное число')

def stepen_s_operatorom(x, y):
    print('Проверка с оператором =')
    print(x**y)

def stepen_bez_operatora(x,y):
    for element in range(abs(y)-1):
        x=x*x
    print('Проверка без оператора =')
    print(1/x)

print('Возведение в степень с помощью оператора "**"')
stepen_s_operatorom(int(proverka_na_deistvitelnoye_i_polozitelnoye(input('Введите число, возводимое в степень '))),
                    int(proverka_na_celoe_i_otricatelnoe(input('Введите степень, в которую будет возводится число '))))
print()
print('Возведение в степень с помощью цикла')
stepen_bez_operatora(int(proverka_na_deistvitelnoye_i_polozitelnoye(input('Введите число, возводимое в степень '))),
                    int(proverka_na_celoe_i_otricatelnoe(input('Введите степень, в которую будет возводится число '))))
