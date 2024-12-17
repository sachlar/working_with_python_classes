# Dog class, class names should always have a capital first letter its pythonic
# A function that is part of a class is called a method

class Dog:
    """simple attempt to model a dog"""
    def __init__(self, name, age):
        """this initialises name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# make an instance from the Dog class

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog {my_dog.name} is {my_dog.age} years old.")

# calling methods
my_dog.sit()
my_dog.roll_over()

# creating multiple instances from a class
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog {my_dog.name} is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog {your_dog.name} is {your_dog.age} years old.")
your_dog.sit()