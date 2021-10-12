seconds = int(input('Введите время в секундах '))
hours = seconds // 3600
minutes = (seconds - hours * 3600)//60
ost_seconds = seconds - hours * 3600 - minutes * 60
print('{}:{}:{}'.format(hours, minutes, ost_seconds))