# Example of a first function to multiply two user input numbers
quotient1 = int(input("please provide a first quotient: "))
quotient2 = int(input("please provide a second quotient: "))

def multiply(x, y):
    """returns the multiplication result of x * y"""
    product = x * y
    return float(product)

multiplicationResult = multiply(quotient1, quotient2)

#show the docstring(=explanation in between the green """ """s) of that function
help(multiply)
#print a functions result for the first time
print(f"the result of your multiplication is = {multiplicationResult}.")



# An example for rising a user input number to its third power
baseNumber = int(input("please provide a base: "))

def cube_of(base):
    """rises a given input to the third power"""
    exponentiation = base ** 3
    return exponentiation

exponentiationResult = cube_of(baseNumber)

# Show the docstring (=explanation of the function)
help(cube_of)
# print the function's result
print(f"the result of rising {baseNumber} to the third power is = {exponentiationResult}.")




# Now an example for greeting a user
yourName = input("What was your name again? ")

def greet_person(name):
    """Take 'greetedPerson' as an argument and return a greeting including his/her name"""
    return f"Ahh yeah right! Hi {name}."

greetOutput = greet_person(yourName)

# Show the docstring (=explanation of the function)
help(greet_person)
# Print the function's result
print(greetOutput)