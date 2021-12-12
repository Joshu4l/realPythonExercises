# EXAMPLE ON HOW TO USE '.super()'
# in order to access the respective parent-Method inmidst of a child definition:


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



# Example on how to call a parent method during a child instantiation
class JackRusselTerrier(Dog):

    # Provide a class specific attribute
    breed = "Jack Russel Terrier"

    # Modify what we received by inheritance
    def bark(self, sound="arff"):

        # SCRAPPY WAY of overwriting the original parent method would be
        # hard-coding the output by ourselves, like:
        # return f"{self.name} barks '{sound}'."

        # MORE EFFICIENT WAY of overwriting the original parent method would be
        # actually accessing the parent's method and redefine it on the spot with our reset parameter (sound):
        return super().bark(sound)


john = Dog("John", 11)  # Instantiate a dog object
print(john)
print(john.bark())


jim = JackRusselTerrier("Jim", 3)  # Instantiate a Jack Russel Terrier object
print(jim)
print(jim.breed)
print(jim.bark())

