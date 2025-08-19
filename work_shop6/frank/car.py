from abc import ABC, abstractmethod
import mymodule as mymodule
class Car():
    year = 2025
    
    def __init__(self,model,brand,owner):
        self.model = model
        self._brand = brand
        self.__owner = owner
        
    def get_owner(self):
        return self.__owner
    
    def set_owner(self,onwer):
        self.__owner = onwer
    
    def print_c(self):
        print("c")
    
    @abstractmethod
    def make_noise(self): 
        pass
    
class fourWDcar(Car):
    def __init__(self, model, brand, owner, engine):
        super().__init__(model, brand, owner)
        self._engine = engine
        
    def print_info(self):
        print(
            self.year,
            self.model,
            self._brand,
            self._engine,
            self.get_owner()
        )
    def print_c(self, input):
        super().print_c()
        print("D")
        print(input)

    def make_noise(self):
        print("this is a making noise method")
        
class Truck(Car):   
    def __init__(self, model, brand, owner):
        super().__init__(model, brand, owner)
    def big_noise(self):
        print("this is big noise")
         
print(mymodule.greeting("Frank"))

car_one = Car("accord", "honda", "winston")
car_two = Car("A6", "Audi", "frank")
fourWDcar_one = fourWDcar("Ranger", "Ford", "john", "V8")
print(fourWDcar_one.model)
print(fourWDcar_one.get_owner())
fourWDcar_one.print_info()

fourWDcar_one.print_c("Hello from fourWDcar")
#car_one.print_c()

fourWDcar_one.make_noise()

# print(car_one.year)
# print(car_two.year)

# print(car_one._brand)
# #print(car_two._brand)
# car_one._brand = "toyota"
# print(car_one._brand)

# print(car_one.get_owner())
# print(car_one.set_owner("john"))
# print(car_one.get_owner())