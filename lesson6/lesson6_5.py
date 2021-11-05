class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title} \n')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой \n')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом \n')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером \n')


pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()