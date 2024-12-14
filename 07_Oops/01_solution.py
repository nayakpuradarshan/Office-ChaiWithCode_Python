class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return print(f"{self.__brand} {self.__model}")

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "car are means of trasport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# my_electric_car = ElectricCar("Tesla", "model x", "85KWH")
# print(isinstance(my_electric_car, ElectricCar))
# print(isinstance(my_electric_car, Car))

# print(my_electric_car.get_brand())
# print(my_electric_car.fuel_type())

# total_car = Car("tata", "herrier")
# total_car.model = "Audi"

# print(total_car.model)

# print(total_car.general_description())
# print(Car.general_description())

# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
#
# my_new_car = Car("Tata", "Herrier")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is enginer"

class ElectricCarTwo(Battery, Engine, Car):
    pass


me_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(me_new_tesla.engine_info())
print(me_new_tesla.battery_info())
