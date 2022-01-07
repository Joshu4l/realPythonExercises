# Demonstration #1 on how try & except work in a while loop.
# We want the user to ONLY enter a NUMERIC value


# Ask the user for a normal input (without any int- or float specs)
my_input = input("your input here: ")

while True:  # As long as we're getting a possible/'True' content for the following attempt of...

    #  ... assigning the number as an integer we're good.
    try:
        number = int(my_input)  # HERE's the crucial line that's trying to assign the input as an INT.
        print(f"Thank you for your input. You've entered {number}.")

        break  # EXIT the loop after we got what we wanted.

    # For the case of encountering a ValueError, continuously ask the user to provide a numeric value
    except ValueError:
        my_input = input("that was not a number, try again: ")
