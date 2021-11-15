class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'Введена правильная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])


today = Data('15 - 11 - 2021')
print(today)
print(Data.extract('26 - 06 - 2014'))
print(today.extract('06 - 11 - 2019'))
print(Data.valid(1, 11, 2000))
print(Data.valid(26, 6, 2021))
print(today.valid(26, 66, 2013))