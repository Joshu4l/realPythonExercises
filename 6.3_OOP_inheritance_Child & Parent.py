# EXAMPLE ON CLASS INHERITANCE:

# A CHILD CLASS CAN 'INHERIT' (RECEIVE) ALL THE ATTRIBUTES AND METHODS FROM THEIR PARENT
# THEN THEY CAN START FROM THERE AND EXTEND OR OVERRIDE WHAT THEY INHERITED FROM THEIR PARENT AT THE BEGINNING
# THEY CAN 'MAKE USE' OF WHAT THEY GOT FOR WHATEVER THEIR INTENTION/PURPOSE IS

# Example for an initial parent class
class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def bark(self, sound):
        return f"{self.name} barks '{sound}'."
        # We won't add a breed attribute here! That would be scrappy when trying to cluster dogs
        # Instead, we're gonna organize ourselves in child classes


# Now we want to have a characteristic bark for every dog breed
# So we're going to create a child class for each breed


# EXAMPLE FOR CREATING THREE CHILD CLASSES:
# (A child class is defined just like a parent class.)
# BUT: What's special about child classes is: they come with PARENTHESES stating their PARENT in it:
class JackRusselTerrier(Dog):
    def bark(self, sound="arff"):  # << HERE is where we define a default value for our inherited class method
        # The rest stays exactly the same as defined in the parent class
        return f"{self.name} barks '{sound}'."

class Dachshund(Dog):
    def bark(self, sound="wff"):
        return f"{self.name} barks '{sound}'."

class Bulldog(Dog):
    def bark(self, sound="woof"):
        return f"{self.name} barks '{sound}'."


# Instead of instantiating our dogs directly from our parent class, we're gonna do it based on our CHILD classes:
miles = JackRusselTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


# Show jim's type:
print(type(jim))
print(jim.bark())
# Check about his instance existence:
print(isinstance(jim, Bulldog))
print(isinstance(jim, Dachshund))



