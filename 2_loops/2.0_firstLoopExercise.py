# Fist loop demonstration on using 'WHILE'
userInput = input("Please put in a number: ")

# Check if the user's input was numeric or not
while userInput.isnumeric() == False:
    print("Thanks for your input... But please choose something NUMERIC!")
    userInput = input("please put a number: ")

# The above was only to cover unintended, with the following line we continue the program like it was actually planned
print(f"Thanks for your input of '{userInput}'. That number belongs to {type(userInput)}!")



# Now a loop demonstration on using 'FOR'
literal = input("put in a string to loop over: ")

# Print me every character in the given literal and its index in there
for character in literal:
    print(f"{character.lower()}  --> that equals index {literal.index(character)} of the literal '{literal}'.")
