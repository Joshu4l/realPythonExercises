# SORTING METHOD:

# Example for sorting a list of strings
colors = ["red", "yellow", "green", "blue"]
print(colors)

colors.sort()  # doesn't have to be declared with a '='
print(colors)


# Example for sorting a list of numbers
numbers = [3, 9, 7, 6, 1, 5]
print(numbers)

numbers.sort()  # doesn't have to be declared with a '='
print(numbers)


# Sorting a list VIA THE OPTIONAL "KEY"-PARAMETER (1/2): using a built-in function
names = ["ben", "joshua", "sarah", "nils"]
print(names)

# "KEY" always takes a 1-argument-functions return-value as its argument (in this case len is a built-in one)
names.sort(key=len)  # the argument-function must always be stated without braces!
print(names)


# Sorting a list VIA THE OPTIONAL "KEY"-PARAMETER (2/2): using a custom function
integer_pairs = [[4, 1], [1, 2], [-9, 0]]
print(integer_pairs)

def get_second_element (element):
    """returns the second element of an iterable"""
    return element[1]

# "KEY" always takes a 1-argument-functions return-value as its argument (in this case we're use our custom function)
integer_pairs.sort(key=get_second_element)  # the argument-function must always be stated without braces!
print(integer_pairs)
