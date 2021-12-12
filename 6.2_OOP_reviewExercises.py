# 1. Modify the Dog class to include a third instance attribute called "coat_color",
#    which stores the color of the dog's coat as a string.

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = str(coat_color)

    def __str__(self):
        """when the object is called it returns a description of the object using its attributes defined above."""
        return f"""{self.name} is {self.age} years old and has a {self.coat_color} coat."""

    def special_talent(self, talent):
        return f"""{self.name}'s special talent is {talent}."""

# See, that the coat_color attribute was added above! Now we'll instantiate an object:
philo = Dog("Philo", 4, "brown")
print(philo)

# Printing the dog's coat color
print(f"""{philo.name}'s coat is {philo.coat_color}.""")


# 2. Create a Car class with two instance attributes: .color which stores a string and .mileage which stores an integer
#    Then instantiate two Car objects - a blue car with 20,000 miles and a red car with 30,000 miles - and print out
#    their colors and mileage. Your output should look like this: "The {color} car has {miles} miles."

# 3. Modify the car class with an instance method called .drive(), which takes a number as an argument and
#    adds that number to the mileage attribute. Test that your solution works by instantiating a car with 0 miles,
#    then call .drive(800) and print the mileage attribute to check that it is set to 800.

class Car:
    def __init__(self, color, mileage):
        self.color = str(color)
        self.mileage = int(mileage)

    def __str__(self):
        return f"""The {self.color} car has {self.mileage} miles."""

    def drive(self, kilometers):
        return f"""After your input, the car drove {self.mileage + int(kilometers)} kilometers in total."""

# Instantiate and print a first object
bmw = Car("black", 20000)
print(bmw)

# Instantiate and print another object
mercedes = Car("Mercedes", 30000)
print(mercedes)

# Instantiate a third object
toyota = Car("blue", 0)
# calling the .drive() method on that object
print(toyota.drive(800))




