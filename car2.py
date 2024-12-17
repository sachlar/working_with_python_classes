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


