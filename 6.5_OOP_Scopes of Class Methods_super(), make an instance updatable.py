# EXAMPLE ON HOW TO KEEP AN OBJECT MAINTAINED/UPDATED WITH NEW VALUES
# (e.g. an AGING person or animal)


# Create a parent class called Dog
class Dog:

    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def bark(self, sound="Woof"):
        return f"{self.name} barks: '{sound}'."

    # EXAMPLE FOR MAKING AN OBJECTS ATTRIBUTE VALUES MAINTAINABLE:
    # By ASSIGNING instead of just RETURNING we can redefine a prior value
    def set_age(self, age):
        self.age = age



# Create a child class and instantiate it
class JackRusselTerrier(Dog):

    breed = "Jack Russel Terrier"

    def bark(self, sound="arff"):
        return super().bark(sound)



jack = JackRusselTerrier("Jack", 8)
print(jack)
jack.set_age(10)
print(jack)



