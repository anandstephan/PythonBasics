class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand


    def full_name(self):
        return self.brand + " "+self.model
    
    def fuel_type(self):
        return "Petrol"


class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Battery"    

tesla = ElectricCar("Tesla","Model S","345Kwh")
print(tesla.fuel_type())

# my_car = Car("Toyota","Carolla")
# print(my_car.full_name())

    