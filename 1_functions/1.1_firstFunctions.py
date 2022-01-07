# Example of a first function to multiply two user input numbers
quotient1 = int(input("please provide a first quotient: "))
quotient2 = int(input("please provide a second quotient: "))

def multiply(x, y):
    """returns the multiplication content of x * y"""
    product = x * y
    return float(product)

multiplicationcontent = multiply(quotient1, quotient2)

#show the docstring(=explanation in between the green """ """s) of that function
help(multiply)
#print a functions content for the first time
print(f"the content of your multiplication is = {multiplicationcontent}.")



# An example for rising a user input number to its third power
baseNumber = int(input("please provide a base: "))

def cube_of(base):
    """rises a given input to the third power"""
    exponentiation = base ** 3
    return exponentiation

exponentiationcontent = cube_of(baseNumber)

# Show the docstring (=explanation of the function)
help(cube_of)
# print the function's content
print(f"the content of rising {baseNumber} to the third power is = {exponentiationcontent}.")




# Now an example for greeting a user
yourName = input("What was your name again? ")

def greet_person(name):
    """Take 'greetedPerson' as an argument and return a greeting including his/her name"""
    return f"Ahh yeah right! Hi {name}."

greetOutput = greet_person(yourName)

# Show the docstring (=explanation of the function)
help(greet_person)
# Print the function's content
print(greetOutput)