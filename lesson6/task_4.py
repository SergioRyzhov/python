class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        print(f'The car start going')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'The car was stopped')
        self.show_speed()

    def turn_direct(self, direction):
        print(f'The car was turned {direction}')

    def show_speed(self):
        print(f'Now speed is: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'You are speeding! {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'You are speeding! {self.speed}')


class PoliceCar(Car):
    pass


town_car = TownCar(65, 'black', 'chevrolet')
sport_car = SportCar(120, 'red', 'ferrari', True)
work_car = WorkCar(45, 'white', 'renault')

print(town_car.name)
print(sport_car.color)
print('\n')
sport_car.go()
sport_car.turn_direct('right')
sport_car.stop()
print('\n')
work_car.go()
work_car.turn_direct('left')
work_car.stop()
