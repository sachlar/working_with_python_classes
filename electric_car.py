# create a Car class
class Car:
    """simple car class"""
    def __init__(self, make, model, year):
        """initialise car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """print the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """set odometer reading to value passed"""
        """reject the change if it trys to roll back the mileage"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the mileage backwards")

    def increment_odometer(self, miles):
        """add given amount to the odometer reading"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# modifying attribute values
# direct way
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# the batter class to de-clutter the electriccar class

class Battery:
    """A simple attempt to model a car battery"""

    def __init__(self, battery_size=40):
        """initialise the batteries attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print statement to describe battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        """show the range of the battery"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

# electric car class inheritted from Car class


class ElectricCar(Car):
    """represents aspects of a car but specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialise attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """electric cars don't have gas tanks so let them know if called"""
        print("This car is electric, it does not have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


