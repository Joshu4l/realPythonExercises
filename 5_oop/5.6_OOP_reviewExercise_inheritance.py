# 1. Create a 'GoldenRetriever'-class, that inherits from the 'Dog'-class.
# Give the 'sound'-argument of 'GoldenRetriever.speak()' a default value of "Bark".

# Use the following code for your parent 'Dog'-class:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} barks: '{sound}'"


class GoldenRetriever(Dog):

    def speak(self, sound="Bark"):
        return super().speak(sound)

rusty = GoldenRetriever("Rusty", 5)
print(rusty)
print(rusty.speak())


# 2. Write a 'Rectangle'-class that must be instantiated with two attributes: '.length' and '.width'
# Add an .area() method to the class that returns the area (length * width) of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle with a length of {self.length} and a width of {self.width}."

    def area(self):
        area = self.length * self.width
        return f"Area counts = {area}"


# Then write a 'Square'-class that inherits from the 'Rectangle'-class and is instantiated
# with a single attribute called 'side_length'.
# Test your 'Square'-class by instantiating a square with a '.side_length' of 4.
# Calling .area() should return 16.
class Square(Rectangle):

    def __init__(self, side_length):

        # Instead of 'length' and 'width'
        # we instantiate our parent class with 'side_length' 2x
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def __str__(self):
        return f"Square with a side length of {self.side_length}"

r1 = Rectangle(7, 5)
print(r1)
print(r1.area())


s1 = Square(4)
print(s1)
print(s1.area())
print(s1.side_length)
print(s1.length)
print(s1.width)

