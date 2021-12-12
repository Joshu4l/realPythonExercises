
# Some things to notice:

# 1. The convention of writing class names is: CapitalLetterNotation

# 2. Classes bundle a bunch of properties, which will be assigned to an object as its respective stem-properties

# 3. An object = an instance of a class

# 4. Every class-body contains the '.__init__()' method for initializing new objects.
#    The initialization is done in order to set the initial state of a variable called "self".
#    After that is done, attributes can actually be assigned to individual instances of that class.


# EXAMPLE ON HOW TO DEFINE A CLASS
class Dog:

    # CLASS attribute
    species = "Canis familiaris"   # (will be assigned to every instance of the dog class)

    def __init__(self, name, age):
        self.name = name  # INSTANCE attribute (will differ from object to object)
        self.age = age    # INSTANCE attribute (will differ from object to object)


# Creating a new object from a class is called "instantiating an object"
rusty = Dog("Rusty", 5)
miles = Dog("Miles", 7)


# After instantiating an object we can now coll their attributes by using dot-notation:
print(rusty.species)
print(rusty.age)
print(miles.species)
print(miles.age)


# In order to change the attribute value of an object we can simply set it by using the '=' operator:
miles.age = 9
print(f"""Now, Miles age is: {miles.age}""")


# Even changing the class attribute value of an object is possible.
# No need to worry that the other objects' class attributes will be changed too ;)
miles.species = "Felis silvestris"
print(f"""Despite we changed Miles' species to {miles.species}, the species of Rusty remains {rusty.species}""")


