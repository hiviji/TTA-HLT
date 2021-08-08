from vehicle import Vehicle
from passengerVehicle import PassengerVehicle

class Bike(PassengerVehicle):
    def __init__(self, max_num_of_passengers):
        self.max_num_of_passengers = max_num_of_passengers