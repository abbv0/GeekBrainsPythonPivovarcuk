"""
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных.

Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.
"""

from pprint import pprint


class Warehouse:
    def __init__(self, title):
        self.title = title
        self.lists = {}

    def broadcast_to_warehouse(self, equipment):
        self.lists.update({equipment.serial_number:[equipment.title, self]})
        print('На склад '+self.title+' получено оборудование:'+ '' +equipment.title)

    def list_equipments(self):
        print('На склад '+self.title + ' получено оборудование:')
        pprint(self.lists)
        print('Общее количество: ', len(self.lists))


class Orgtrchnika:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(Orgtrchnika):
    def __init__(self,title, serial_number, print_velocity):
        Orgtrchnika.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название :'+Orgtrchnika.__str__(self) + ' ,Параметр: ' +str(self.print_velocity)


class Scanner(Orgtrchnika):
    def __init__(self, title, serial_number, resolution):
        Orgtrchnika.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название :'+Orgtrchnika.__str__(self) + ' ,Параметр: ' +str(self.resolution)


class Copier(Orgtrchnika):
    def __init__(self, title, serial_number, addit):
        Orgtrchnika.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название :'+Orgtrchnika.__str__(self) + ' ,Параметр: ' +str(self.addit)


store1 = Warehouse('Warehouse_1')
store2 = Warehouse('Warehouse_2')
printer1 = Printer('Xerox', 9999, 1)
scanner1 = Scanner('HP', 8888, 2)
copier1 = Copier('Pantum', 7777, 3)
copier2 = Copier('Novex', 6666, 4)

print(printer1)
print(scanner1)
print(copier1)
print(copier2)

store1.broadcast_to_warehouse(printer1)
store1.broadcast_to_warehouse(scanner1)
store1.broadcast_to_warehouse(copier1)
store1.broadcast_to_warehouse(copier2)
store2.broadcast_to_warehouse(copier1)
store2.broadcast_to_warehouse(copier2)
print('')
store1.list_equipments()
print('')
store2.list_equipments()
