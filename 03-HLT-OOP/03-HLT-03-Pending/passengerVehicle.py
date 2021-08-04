from vehicle import Vehicle

class PassengerVehicle(Vehicle):
    def __init__(self, max_num_of_passengers):
        self.max_num_of_passengers = max_num_of_passengers