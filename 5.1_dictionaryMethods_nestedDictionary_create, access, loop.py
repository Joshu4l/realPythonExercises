# Creating a nested dictionary by writing a dictionary literal:
fellows = {
    "Human": {
        "representative": "Aragorn",
        "habitat": "Gondor",
        "weapon of choice": "Sword"
    },

    "Hobbit": {
        "representative": "Frodo",
        "habitat": "Auenland",
        "weapon of choice": "Sword"
    },

    "Dwarf": {
        "representative": "Gimli",
        "habitat": "Moria",
        "weapon of choice": "Axe"
    },

    "Elve": {
        "representative": "Legolas",
        "habitat": "Bruchtal",
        "weapon of choice": "Longbow"
    },

    "Nazgul": {
        "representative": "Witchking of Angmar",
        "habitat": "Angmar",
        "weapon of choice": "Flail"
    }
}
# Let's inspect how our dictionary will be printed:
print(fellows)  # this is how it will look like without further formatting

import json
fellows_formatted = json.dumps(fellows, sort_keys=True, indent=4)
print(fellows_formatted)  # this is how it looks like after the json-library's formatting method.


# EXAMPLE FOR LOOPING OVER A NESTED DIRECTORY:
# looping over the top-level of our key-value-pairs
for keys, values in fellows.items():  # getting both parts of our key-value-pair here
    print(f"""CREDENTIALS FOR DICTIONARY-KEY '{keys}':""")  # printing only the key

    for nested_kvp in values.items():  # looping over every inner(nested) kvp of our top-level-values...
        print(f"""- {nested_kvp[1]}""")  # ... and printing only the second item from in there


