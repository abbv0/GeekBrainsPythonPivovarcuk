"""
Реализовать класс Road (дорога).
 
    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
    проверить работу метода.
"""

class Road:
    _lenght: int
    _width: int
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def formula(self):
        print(self._lenght*self._width*25*5/1000)

road1 = Road (20, 5000)
road1.formula()
