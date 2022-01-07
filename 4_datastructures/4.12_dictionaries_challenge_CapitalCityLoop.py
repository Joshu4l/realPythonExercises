# Review your state capitals along with your knowledge of dictionaries and while 2_loops!

# First, fill a dictionary literal with states and capitals and their associated capitals.
# Also extend the dictionary by values of our previous file.

# Next, pick a random key name from the dictionary and assign both: the state and its capital to two variables.
# You'll need to   import the random module   at the top of your program.

# Then display the name of the state to the user and ask them to enter the capital. If the user answers incorrectly,
# then repeatedly ask them for the capital until they either enter the correct answer or type "exit".

# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without
# guessing correctly, display the correct answer and the word "Goodbye".

#     NOTE:
#     Make sure the user isn't punished for case sensitivity.
#     In other words, a guess of "Denver" is the same as "denver".
#     Do the same for exiting -> "EXIT" and "Exit" should work the same as "exit".



capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

missing_capitals = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin")
)

for i in missing_capitals:
    missing_state = i[0]
    missing_capital = i[1]
    capitals_dict[missing_state] = missing_capital

import json
print(json.dumps(capitals_dict, sort_keys=True, indent=4))


import random
extracted_item = random.choice(list(capitals_dict.items()))  ## important to turn our choice into a LIST!

extracted_state = extracted_item[0]
extracted_capital = extracted_item[1]


while True:
    user_guess = input(f"""Guess the capital of -> {extracted_state}: """)

    if user_guess.lower() == extracted_capital.lower():
        print(f"""Correct! The capital of {extracted_state} is {user_guess}. :)""")
        break

    elif user_guess.lower() == "exit":
        print(f"Alright, thanks for participating anyway.")
        print(f"""Solution would've been: {extracted_state} -> {extracted_capital}""")
        break

    else:
        print(f"""Sorry, that's not correct - Try that again!""")
