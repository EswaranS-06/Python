class Vehicle():
    def __init__(self, speed, tank_capacity, total_distance, name, color, type, no_of_wheels):  # mileage, color, engine
        self.speed = speed
        self.name = name
        self.type = type
        self.no_of_wheels = no_of_wheels
        self.tank_capacity = tank_capacity
        self.total_distance = total_distance
        self.color = color

    def forward(self):
        print(f"[{self.name}] Move Forward")

    def backward(self):
        print(f"[{self.name}] Move Backward")

    def left(self):
        print(f"[{self.name}] Move Left Side")

    def right(self):
        print(f"[{self.name}] Move Right Side")

    def __str__(self):
        return (f'''
              {self.type}
            -------
                Name: {self.name}
                Color: {self.color}
                Mileage: {self.total_distance // self.tank_capacity} km/liter
                Tank size: {self.tank_capacity} liter
                No of Wheel: {self.no_of_wheels}
                distance cover: {self.total_distance} km             
              ''')


# Car Class Inherte

class car(Vehicle):
    def __init__(self, speed, color, name, tank_capacity, total_distance):
        super().__init__(speed, tank_capacity, total_distance, name, color, type='Car', no_of_wheels=4)


class bike(Vehicle):
    def __init__(self, speed, color, name, tank_capacity, total_distance, wheels=2):
        super().__init__(speed, tank_capacity, total_distance, name, color, type='Bike', no_of_wheels=wheels)

    #    def __init__(self, speed, color, name, tank_capacity, total_distance, wheels):
    #        self.name = name
    #        self.color = color
    #        super().__init__(speed, wheels, tank_capacity, total_distance, name)

    def backward(self):
        print(f"[{self.name}] Sorry, Push the Bike backwarks by yourself")


car1 = car(80, 'Red', 'Volvo', 10, 400)
car2 = car(120, 'Black', 'Suzuki', 12, 300)
bike1 = bike(100, 'White', 'Yamaka', 5, 300)
atv = bike(80, 'Blue', 'Tri-Maki', 7, 200, wheels=4)

car1.left()
print()
car1.backward()
print()
car1.right()
print()
car2.forward()
print()
car2.right()
print()
bike1.forward()
print()
bike1.backward()
print()
atv.right()
print()
print(car1)
print(car2)
print(bike1)
print(atv)
