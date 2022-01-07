# First possible way of creating a dictionary: WRITING A DICTIONARY LITERAL
dictionary_via_literal = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Albany"
}
print(dictionary_via_literal)
print(type(dictionary_via_literal))


# Second possible way of creating a dictionary: USING THE DICT-METHOD
# E.g. setting up a nested tuple first
tuple_sequence = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin")
)
# Now we'll transform the tuple into a dictionary by using the 'dict()'-method
dictionary_via_dict_method = dict(tuple_sequence)
print(dictionary_via_dict_method)
print(type(dictionary_via_dict_method))


# DELETING DICTIONARY ENTRIES:
# Setting up a dictionary literal first
dictionary_via_literal = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"
}
# Now we use python's built-in "del"-function to DELETE a certain key:
del dictionary_via_literal["Texas"]
print(dictionary_via_literal)  # Texas is gone now


# Example for REASSIGNING dictionary values:
dictionary_via_literal["New York"] = "Brooklyn"
print(dictionary_via_literal)


# ACCESSING DICTIONARY VALUES:
# Setting up a sample dictionary
fellows = {
    "Human": "Aragorn",
    "Hobbit": "Frodo",
    "Dwarf": "Gimli",
    "Elve": "Legolas",
    "Nazgul": "Witchking of Angmar"
}


# KEY NOTATION - ACCESSING values via a certain dictionary key:
print(fellows["Nazgul"])  # Note that we have to state the dictionary KEY here INSTEAD OF AN INDEX!


# DICTIONARY-METHOD 1 - ACCESSING all existing KEY-VALUE-PAIRS (items) in the dictionary:
# Probably the most powerful method!
print(fellows.items())  # will be returned in a list format

# DICTIONARY-METHOD 2 - ACCESSING all existing KEYS in the dictionary:
print(fellows.keys())  # will be returned in a list format

# DICTIONARY-METHOD 3 - ACCESSING all existing VALUES in the dictionary:
print(fellows.values())  # will be returned in a list format


# LOOPING OVER DICTIONARIES BY USING A "for"-LOOP:
for key, value in fellows.items():  # making use of the fact, that there are only 2 possible assignments
    print(f"""dictionary key: {key}, dictionary-value: {value}""")

for key, value in fellows.items():  # only printing one our keys
    print(key)

for key, value in fellows.items():  # only printing one our values
    print(value)
