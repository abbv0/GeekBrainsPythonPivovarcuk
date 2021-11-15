import sys

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите значения через Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                last_question = input(f'Попробовать еще раз? Y/N ')

                if last_question == 'Y' or last_question == 'y':
                    print(try_except.my_input())
                else:
                    return f'До свидания'
                    sys.exit()

try_except = Error(1)
print(try_except.my_input())