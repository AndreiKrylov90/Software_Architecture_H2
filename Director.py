class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_sports_car(self):
        return self.builder.set_seats(2).set_engine_power("500 hp").set_child_seat(False).get_car()

    def build_family_car(self):
        return self.builder.set_seats(6).set_engine_power("200 hp").set_child_seat(True).get_car()

    def build_taxi_car(self):
        return self.builder.set_seats(4).set_engine_power("100 hp").set_child_seat(False).get_car()