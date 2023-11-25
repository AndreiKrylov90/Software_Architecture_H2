class Car:
    def __init__(self):
        self.seats = None
        self.engine_power = None
        self.has_child_seat = None

    def __str__(self):
        return (f"Seats - {self.seats}, Engine Power - {self.engine_power}, "
                f"Child Seat - {self.has_child_seat}")

