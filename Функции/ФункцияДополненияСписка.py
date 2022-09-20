"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму 
этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def my_sum ():
    sum_result = 0
    proverka = False
    while proverka == False:
        number = input('Input numbers or "e" for quit - ').split()
        result = 0
        for e in range(len(number)):
            if number[e] == 'e' or number[e] == 'E':
                proverka = True
                break
            else:
                result = result + int(number[e])
        sum_result = sum_result + result
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')


my_sum()
