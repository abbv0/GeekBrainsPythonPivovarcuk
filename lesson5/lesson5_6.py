# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по
# этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.

subjects = {}

try:
    with open('lesson_5_6_file', 'r') as file6:
        for line in file6.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)
except ValueError:
    print("VaLuEeRrOr")

print(subjects)
