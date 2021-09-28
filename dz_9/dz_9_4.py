import random


class Car:
    speed = random.randint(1, 200)

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self):
        direction = random.choice(['right', 'left'])
        print(f'{self.name} turn {direction}')

    def show_speed(self):
        print(f'Speed {self.name} {Car.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if super().speed > 60:
            print(f'Speed {super().speed} is too high ')
        else:
            print(f'Speed car {super().speed} km/h')


class SportCar(Car):
    '''''sport car'''


class WorkCar(Car):

    def show_speed(self):
        if super().speed > 40:
            print(f'Speed {super().speed} is too high ')
        else:
            print(f'Speed car {super().speed} km/h')


class PoliceCar(Car):
    is_police = True


car = Car('Lexus', 'red')
town_car = TownCar('Renault', 'yellow')
sport_car = SportCar('Ferrary', 'violet')
work_car = WorkCar('Man', 'orange')
police_car = PoliceCar('Ford', 'black')

cars = [car, town_car, sport_car, work_car, police_car]

for n in cars:
    print(n.name, n.color)
    n.go()
    n.show_speed()
    n.turn()
    n.stop()
