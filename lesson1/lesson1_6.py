a = int(input('Введите количество километров в первый день '))
b = int(input('Введите количество километров нужный результат '))
denb = 1
print('1-й день: {}'.format(a))
while a < b:
    a = 1.1 * a
    denb = denb + 1
    print('{}-й день: {:.2f}'.format(denb, a))
print()
print('на {} день мы достигли результата'.format(denb))