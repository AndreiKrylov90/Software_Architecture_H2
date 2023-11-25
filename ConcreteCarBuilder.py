from Car import Car
from CarBuilder import CarBuilder


class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_seats(self, seats):
        self.car.seats = seats
        return self

    def set_engine_power(self, engine_power):
        self.car.engine_power = engine_power
        return self

    def set_child_seat(self, has_child_seat):
        self.car.has_child_seat = has_child_seat
        return self

    def get_car(self):
        return self.car
