proceeds = int(input('Введите выручку фирмы '))
costs = int(input('Введите издержки фирмы '))
if proceeds <= costs:
    print('Компания не получила прибыли')
else:
    print('Компания получила прибыль')
    earnings =proceeds-costs
    profitability = earnings/proceeds
    number_of_employees = int(input('введите количество сотрудников '))
    earnings_per_employee = earnings/number_of_employees
    print('Рентабельность фирмы {:.3f}, прибыль на сотрудника {:.3f}'.format(profitability,earnings_per_employee))
