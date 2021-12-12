# EXAMPLE ON HOW TO DEFINE INSTANCE METHODS
class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # SETTING UP A USER DEFINED FUNCTION WITHIN A CLASS DEFINITION EQUALS AN INSTANCE'S METHOD!

    # EXAMPLE OF AN INSTANCE-"DUNDER-"METHOD (because it begins and starts with double underscores)
    # CAUSES THE DESCRIPTION BELOW TO BE PRINTED WHEN SIMPLY TYPING THE OBJECT'S NAME:
    def __str__(self):
        """returns a description of the object using its attributes defined above."""
        return f"""{self.name} is {self.age} years old."""

    # 2nd EXAMPLE OF AN INSTANCE METHOD:
    def special_talent(self, talent):  # Introducing a new input parameter (has to be stated when calling the method)
        return f"""{self.name}'s special talent is {talent}."""


# Instantiating an object called 'rusty'
rusty = Dog("Rusty", 5)


# Printing the instance methods for our object 'rusty':
print(rusty)  # remember: when typing the object's name, a description will be printed! That's what we defined
print(rusty.special_talent("finding hidden treats"))

