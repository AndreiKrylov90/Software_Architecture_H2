# Создаем программу, которая создает экземпляр класса Машина с использование паттерна Buider.

from ConcreteCarBuilder import ConcreteCarBuilder
from Director import Director

if __name__ == '__main__':
    builder = ConcreteCarBuilder()
    director = Director(builder)

    sports_car = director.build_sports_car()
    print("Sports Car:", sports_car)

    family_car = director.build_family_car()
    print("Family Car:", family_car)

    taxi_car = director.build_taxi_car()
    print("Taxi Car:", taxi_car)

    # создаем нетиповую машину без класса Director
    party_bus = builder.set_seats(8).set_child_seat(False).set_engine_power("145 hp").get_car()
    print("Party bus:", party_bus)
