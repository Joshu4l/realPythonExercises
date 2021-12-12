# Challenge: Model a farm
# In this assignment, you'll create a simplified model of a farm.
# As you work through this assignment, keep in mind there are a number of correct answers!

# The focus of this assignment is less about the Python class syntax and more about
# software design in general, which is highly subjective.
# This assignment is intentionally left open-ended to encourage you to think about
# how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes,
# attributes and methods. Think about inheritance. How can you prevent code duplication.
# Take the time to work through as many iterations as you feel are necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

# 1. You should have at least four classes: The 'Animal' parent class and at least three child animal classes
#    which inherit from 'Animal'

# 2. Each class should have a few attributes and at least one method that models some behavior
#    appropriate for a specific animal or all animals - walking, running, eating, sleeping etc.

# 3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors

# Define a parent class
class Animal:

    # Class attributes
    position = 1
    walk_increment = 0

    stuff_in_belly = 0
    food_portion = 1

    # Initializer
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"name: {self.name}, color: {self.color}"


    # Introduce the attribute  <sound>  and (optionally) initialize it
    def talk(self, sound=None):
        """ Returns the string: '<name> says <sound>.' """

        # If <sound> is left out, return only "Hello, I'm <name>"
        if sound is None:
            return f"Hello. I'm {self.name}!"
        # Else: return the whole string:  <name> says <sound>
        else:
            return f"{self.name}'s sound: '{sound}'; "

    # Introduce the attribute  <walk_increment>  and initialize it
    def move(self, walk_increment):

        self.position = self.position + walk_increment
        return f"{self.name} moved {walk_increment} positions."


    def need_to_feed(self):

        if self.stuff_in_belly < 2:
            # If the ATTRIBUTE-value is less than 2, state that the animal is hungry
            return f"{self.name} is hungry"
        else:
            # Else, state the animal is not hungry
            return f"{self.name} is not hungry"


    def feed(self, food_portion):

        self.stuff_in_belly = self.stuff_in_belly + food_portion

        if self.stuff_in_belly >= 2:
            # If the ATTRIBUTE-value got bigger than 2, let the animal poop
            return f"{self.name} was fed {food_portion} food portion: {self.poop()}"
        else:
            # Else, feed it its custom food portion
            return f"{self.name} was fed {food_portion} food portion. Portions currently in belly: {self.stuff_in_belly}"


    def poop(self):

        self.stuff_in_belly = 0
        return "Ate too much ... belly content was set to 0 in the bathroom"




# 1st child class
class Dog(Animal):

    # Customize how the dog talks by setting a default for <sound>
    def talk(self, sound="Bark Bark!"):
        return super().talk(sound)

    # Customize the dog's walking distance by setting a default for <walk_increment>
    def move(self, walk_increment=3):
        return super().move(walk_increment)

    # Customize the dog's individual food portion
    def feed(self, food_portion=0.5):
        return super().feed(food_portion)



# 2nd child class
class Sheep(Animal):

    # Customize how the sheep talks by setting a default for <sound>
    def talk(self, sound="Meh"):
        return super().talk(sound)

    # Customize how far the sheep walks by setting a default for <walk_increment>
    def move(self, walk_increment=2):
        return super().move(walk_increment)



# 3rd child class
class Pig(Animal):

    # Customize how the pig talks by setting a default for <sound>
    def talk(self, sound="Oink Oink"):
        return super().talk(sound)

    # Customize how far the pig walks by setting a default for <walk_increment>
    def move(self, walk_increment=1):
        return super().move(walk_increment)



# Create a Dog instance
rusty = Dog("Rusty", "yellow")
print(rusty)
print("\n")

# At which position does the dog stand?
print(f"{rusty.name}'s position: {rusty.position}")
print("\n")

# Let the dog move:
print(rusty.move())
# At which position does the dog stand now?
print(f"{rusty.name}'s position now: {rusty.position}")
print("\n")

# Is the dog hungry?
print(rusty.need_to_feed())
print("\n")

# Feed the dog
print(rusty.feed())
# Check if the dog is still hungry?
print(rusty.need_to_feed())
# Feed the dog more
print(rusty.feed())
# Check if the dog is still hungry?
print(rusty.need_to_feed())
# Feed the dog more
print(rusty.feed())
# Check if the dog is still hungry?
print(rusty.need_to_feed())
# Feed the dog more
print(rusty.feed())
print("\n")

# Show how far a dog moves at a time
print(rusty.move())

shaun = Sheep("Shaun", "white")
# Show how far a sheep moves at a time
print(shaun.move())

carl = Pig("Carl", "pink")
# Show how far a pig moves at a time
print(carl.move())



