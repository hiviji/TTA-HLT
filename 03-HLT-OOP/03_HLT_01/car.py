class Car:
    
    def __init__(self, manufacturer,current_gear, max_speed, current_speed):
        self.manufacturer = manufacturer
        self.current_gear = current_gear
        self.max_speed = max_speed
        self.current_speed = current_speed

        if self.current_speed < 0:
            raise ValueError(f"Error: Speed {self.current_speed} cannot be less than zero")

        if self.current_gear not in [0,1,2,3,4,5]:
            raise ValueError(f"Error: {current_gear} not a valid gear to set")

        if self.current_speed > self.max_speed:
            raise ValueError(f"Error: {current_speed} is can not exceed {max_speed}")

    # For all instance methods the first parameter is self
    def __str__(self):
        return f" {self.manufacturer} {self. current_gear} {self.max_speed} {self.current_speed}"

    def speed_up(self, increment):
        if(self.current_speed+increment > self.max_speed):
            raise ValueError(f"ERROR: new speed {self.current_speed+increment}. Speed cannot exceed {self.max_speed}")
        self.current_speed += increment

    def slow_down(self, decrement):
        if(self.current_speed-decrement <= 0):
            raise ValueError("Error, minimum speed must be greater than zero")
        self.current_speed -= decrement
        
    def change_gear(self, new_gear):
            if new_gear not in [0,1,2,3,4,5]:
                raise ValueError(f"Error,{new_gear} not a valid gear change")
            self.current_gear = new_gear