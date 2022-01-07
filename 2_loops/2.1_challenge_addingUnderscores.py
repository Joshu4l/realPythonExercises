# Create an input variable for a string
word = input("Please provide a word that you wish had underscores: ")

# Define a function that adds underscores in between all characters of an input-string
def add_underscores(word):
    """Stores the inner function's content into this enclosing/outer function"""

    # Set up an EMPTY string-variable to later fill it via the for-loop below
    transformed = ""

    # Create a for-loop that takes the len() of the input-word as its upper RANGE
    for i in range(0, len(word)):

        # Now use the empty variable 'transformed'
        # Fill it up with characters from our input-word
        # Each character is represented by the index it has in its container
        transformed = transformed + word[i] + "_"

    return transformed

print(f"This is how it looks with underscores: {add_underscores(word)}")
