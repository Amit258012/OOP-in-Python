class Car:
    def start(self):
        print("Car is starting")

    def go(self):
        print("Car is going")


class Flyable:
    def start(self):
        print("Start the flying object")

    def fly(self):
        print("Flying")


# from left to right it will check
class FlyingCar(Car, Flyable):
    def start(self):
        super().start()


if __name__ == "__main__":
    flying_car = FlyingCar()
    flying_car.start()
