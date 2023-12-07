from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, company, model, year, num_wheels, speed):
        self.__company = company
        self.__model = model
        self.__year = year
        self.__num_wheels = num_wheels
        self.__speed = speed

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    @property
    def company(self):
        return self.__company

    @property
    def model(self):
        return self.__model

    @property
    def year_release(self):
        return self.__year

    @property
    def num_wheels(self):
        return self.__num_wheels

    @property
    def speed(self):
        return self.__speed


class Motorcycle(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year, num_wheels=2, speed=0)

    def test_drive(self):
        self.__speed = 75

    def park(self) -> None:
        self.__speed = 0


class Car(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year, num_wheels=4, speed=0)

    def test_drive(self):
        self.__speed = 60

    def park(self):
        self.__speed = 0
