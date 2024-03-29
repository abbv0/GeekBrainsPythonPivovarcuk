"""
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

russian = {'One' : 'Один',
           'Two' : 'Два',
           'Three' : 'Три',
           'Four' : 'Четыре'}
new_file = []
with open('file_4', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + '  ' + i[1])
    print(new_file)

with open('new_file_4', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
