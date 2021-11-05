class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала \n')

    def stop(self):
        print(f'Машина {self.name} остановилась \n')

    def turn_left(self):
        print(f'Машина {self.name} повернула налево \n')

    def turn_right(self):
        print(f'Машина {self.name} повернула направо \n')

    def show_speed(self):
        print(f'Машина {self.name} развила скорость {self.speed} \n')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Городская машина {self.name} развила скорость {self.speed}')
        if self.speed > 40:
            print(f'Машина {self.name} превысила скорость ')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'\nРабочая машина {self.name} развила скорость {self.speed}')
        if self.speed > 60:
            print(f'Машина {self.name} превысила скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'\n{self.name} является служебной машиной')
        else:
            print(f'\n{self.name} не является служебной машиной')

avto_1 = SportCar(250, 'yellow', 'lamborghini_Urus', False)
avto_2 = TownCar(39, 'black', 'lada_priora', True)
avto_3 = WorkCar(80, 'green', 'hyundai_solaris', False)
avto_4 = PoliceCar(70, 'white',  'UAZ_patriot', True)

avto_1.go()
avto_2.stop()
avto_3.turn_left()
avto_4.turn_right()
avto_2.show_speed()
avto_1.show_speed()
avto_3.show_speed()
avto_4.police()