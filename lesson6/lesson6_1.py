import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор показывает '
                  f'{TrafficLight.__color[i]} ')
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()