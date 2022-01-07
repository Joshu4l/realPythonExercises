# Create a variable for the user's nickname input
nickname = input("type in an 8-digit user name here: ")

# As long as the nickname doesn't consist of exactly 8 characters, demand it again
while not len(nickname) == 8:
    print("Nope, that weren't 8 characters of length. Try again.")
    nickname = input("type in an 8-digit user name: ")

print(f"Thanks, you've chosen '{nickname}' as your nickname.")




# Create a variable for the user's password input
pw = input("Alright, now set a 4 digit password: ")

# As long as the password doesn't consist of exactly 4 characters, demand it again
while not len(pw) == 4:
    print("Again: your password has to be 4 digits of length. Try again.")
    pw = input("Alright, now set a 4 digit password: ")


print("Thank you very much! Your account will be created. :)")