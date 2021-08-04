from car import Car

car1 = Car("Ford", 3, 110, -10)
car2 = Car("Toyota", 5, 100, 40)

car1.change_gear(3)

car2.change_gear(7)

car1.speed_up(180)

car2.slow_down(50)

print(car1)
print(car2)