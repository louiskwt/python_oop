class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep! Beep!')


class Truck(Vehicle):
    def __init__(self, price, gas, color, tire):
        super().__init__(price, gas, color)
        self.tire = tire

    def beep(self):
        print('Honk! Honk!')


honda = Car(1000, 'basic', 'red', 100)
honda.beep()
print(honda.speed)

volvo = Truck(1000, 'basic', 'red', 6)
volvo.beep()
