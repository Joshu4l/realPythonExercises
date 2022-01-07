# Demonstration #2 on how try & except work in a while loop.
# We want the user to state a string first, and after that an index to display the respective character within his word


# Ask the user for a normal input (without any int- or float specs)
stringInput = input("Type a word: ")

# Ask the user for an index input (in this case it's still a string)
indexInput = input("What character position shall be displayed: ")


while True:  # As long as we're getting a possible/'True' content for the following attempt of...

    #  ... assigning the indexInput as an integer we're good.
    try:
        character = int(indexInput)
        print(f"Thanks. The character you're targeting is: '{stringInput[character]}'.")

        break  # EXIT the loop after we got what we wanted.

    # For the case of encountering a ValueError, continuously ask the user to provide an index value that's numeric
    except ValueError:
        indexInput = input("Your index specification has to be numeric. Try again: ")

    # For the case of encountering an IndexError, continuously ask the user to provide an index that's within bounds
    except IndexError:
        indexInput = input("Didn't work. Make sure the targeted character still lies within your word-length: ")
