"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

def summary():
    try:
        with open('file_5', 'w+') as file_obj:
            line = input('Введите цифры через пробел - ')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Файловая ошибка')
    except ValueError:
        print('ValueErOrR')
summary()
