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
