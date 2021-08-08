from vehicle import Vehicle
from transporterVehicle import TransporterVehicle

class Truck(TransporterVehicle):
    def __init__(self, num_of_axles):
        self.num_of_axles = num_of_axles