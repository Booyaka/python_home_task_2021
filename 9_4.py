"""Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.

"""


class Car:
    direction = input('What direction your car need? ')

    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Car: {name}. Color: {color}. Speed: {speed}. Is this a police car? {is_police}')

    def go(self):
        print(f'Car {self.name} on drive!')

    def stop(self):
        print(f'Car {self.name} just stop.')

    def turn(self):
        print(f'Car {self.name} turned {self.direction}')

    def show_speed(self):
        print(f'Car {self.name} is moving at a speed of {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Car {self.name} is moving to fast! Max speed is 60' if self.speed > 60 else super().show_speed())


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Car {self.name} is moving to fast! Max speed is 40' if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'black', 'BMW')
sport_car = SportCar(100, 'red', 'Ferrari')
work_car = WorkCar(30, 'green', 'Ford')
police_car = PoliceCar(50, 'white', 'Ford')

my_list = [town_car, sport_car, work_car, police_car]
for i in my_list:
    i.go()
    i.show_speed()
    i.turn()
    i.stop()
    print('*' * 10)