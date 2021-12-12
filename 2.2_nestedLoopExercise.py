# Create a variable for the user's number input
numberInput = float(input("Please provide a number: "))

# Create a variable for the user's repetition input
repetitionInput = int(input("How often should that be doubled: "))


def wished_double():
    """Stores the inner function's result into this enclosing/outer function"""

    def function_for_looping():
        """Calculates some tasks then hands the result to the enclosing/outer function above"""

        # Important step to get the (outside-) values from the global scope in here
        # They can then be used in the local scope of the loop-function as local variables for calculations
        num = numberInput
        rep = repetitionInput

        for i in range(1, rep+1):
            num = num * 2

        # Return section of the inner(!) function 'function_for_looping'
        return num

    # Return value of the outer function = CALL of the inner function 'function for looping' which does sth when called.
    return function_for_looping()


# All in all result can be stored in a local variable
# By having an input pulled into the above function we actually already have passed values to it
# Hence we're using an 'empty' function here
overallResult = wished_double()

# Print only the local variable (containing the result of the 'wished double'-function)
print(overallResult)
