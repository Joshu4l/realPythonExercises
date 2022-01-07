# Create a variable for the user's number input
number = int(input("Please put in a number here: "))
repetitionTimes = int(input(f"How many times would you like {number} to be doubled? Provide a repetition number: "))


# Define a function that doubles a given number ONCE
def double(num):
    """doubles a given number"""
    res = num * 2
    return res


# Store the first output of the double function into the following variable
doublecontent = double(number)


# Create a loop to run the double-function three times (taking itself as an input)
for loop in range(repetitionTimes):
    print(doublecontent)
    doublecontent = double(doublecontent)



