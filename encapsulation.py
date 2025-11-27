class Car:
    def __init__(self, color, speed, car_id):
        self.color = color
        self.__speed = speed
        self.__car_id = car_id
    
    def set_color(self, new_color):
        self.color = new_color
        
    def set_speed(self, new_speed_car):
        self.__speed = new_speed_car
        
    def get_speed(self):
        self.__private_method()
        return self.__speed
    
    def __private_method(self):
        print('this is private method')
    
car1 = Car('white', 200, 3255)
print(car1.get_speed())

car1.set_speed(305)
# car1.__speed = 300
print(car1.get_speed())
# print(car1.__private_method())
# car1.set_car_id(718)
# print(car1)

# print(car1.get_speed())