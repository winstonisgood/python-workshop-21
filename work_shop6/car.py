from abc import ABC, abstractmethod

class Car(): # template
    year = 2025
    def __init__(self, model, brand, owner):
        self.model = model # public
        self._brand = brand # protected
        self.__owner = owner # private
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def print_c(self):
        print("c")

    @abstractmethod
    def make_noise(self):
        pass
def this_function():
    print("123")

class FOURWDCar(Car):
    def __init__(self, model, brand, owner, engine_number):
        super().__init__(model, brand, owner)
        self._engine_number = engine_number
    
    def print_information(self):
        print(self.year, self.model, self._brand, self.get_owner())
    
    def print_c(self, input):
        super().print_c()
        print("d")
        print(input)

    def make_noise(self):
        print("this is makeing light noise")


class Truck(Car):
    def __init__(self, model, brand, owner):
        super().__init__(model, brand, owner)
    
    def make_noise(self):
        print("this is makeing big noise")


car_one = Car("accord", "honda", "winston")
car_two = Car("A6", "audi", "Frank")
fourwd_car_one = FOURWDCar("a", "b", "c", 123)
# car_one.print_c()
# fourwd_car_one.print_c("this is new function")

car_one.make_noise()
fourwd_car_one.make_noise()
# print(fourwd_car_one._brand)
# print(fourwd_car_one.year)
print(fourwd_car_one.get_owner())
# fourwd_car_one.print_information()

# print(car_one.year)
# print(car_two.year)

# print(car_one.model)
# print("before: ", car_one._brand)
# car_one._brand = "audi"
# print("after: ",car_one._brand)
# print(car_one.__owner)

# print(car_one.get_owner())
# car_one.set_owner("cassy")
# print(car_one.get_owner())