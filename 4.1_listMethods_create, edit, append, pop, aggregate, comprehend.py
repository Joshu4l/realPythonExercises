# First possible way of creating a list: WRITING A LIST LITERAL
list_via_literal = [1, "two", 3.0]
print(list_via_literal)


# Second possible way of creating a list: THE LIST METHOD
list_via_method = list([1, "two", 3.0])
print(list_via_method)


# Third possible way of creating a list: STRING SPLITTING
string_with_delimiters = "this, is, a, whole, sentence, containing, delimiters"
print(string_with_delimiters)

list_via_split_commas = string_with_delimiters.split(", ")
print(list_via_split_commas)

string_with_spaces = "this is a whole sentence using spaces"
print(string_with_spaces)

list_via_split_spaces = string_with_spaces.split(" ")
print(list_via_split_spaces)


# COUNT THE ELEMENTS in an existing list
list_to_be_counted = [1, "2", 3.7, "four"]
count_of_list_elements = len(list_to_be_counted)
print(count_of_list_elements)


# CHANGING elements in an existing list
list_to_be_edited = ["yellow", "red", "green", "blue"]
print(list_to_be_edited)

list_to_be_edited[0] = "purple"  # Change only one element specified by its index
print(list_to_be_edited)

list_to_be_edited[0:4] = ["white", "black", "grey"]  # Change a list of 4 by an input of only 3
print(list_to_be_edited)


# INSERTING elements into an existing list (works like inserting columns)
existing_list = [1, 1.5, 2, 2.5, 3, 4]
print(existing_list)

existing_list.insert(5, 3.5)  # First, state the position where to insert and then the value to be inserted
print(existing_list)


# POP elements from an existing list (deletes a targeted element by stating its index)
colors = ["white", "black", "grey", "gold"]
print(colors)

colors.pop(2)  # delete an element specified by its index
print(colors)

colors.pop()  # stating empty brackets only deletes the LAST element from the list
print(colors)


# APPEND ONE ELEMENT to the end of an existing list
animals = ["fox", "dog", "bear"]
print(animals)

animals.append("wolf")  # appending a single element
print(animals)


# EXTEND an existing list by MULTIPLE ELEMENTS
fruits = ["apple", "pear", "strawberry"]
print(fruits)

fruits.extend(["banana", "orange"])  # extend the list by several elements
print(fruits)


# NUMBER-RELATED METHOD 1: SUM
numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers_total = sum(numbers)  # similar to an excel sum function
print(numbers_total)


# NUMBER-RELATED METHOD 2: MIN
numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers_minimum = min(numbers)  # return the smallest number in a list
print(numbers_minimum)


# NUMBER-RELATED METHOD 3: MAX
numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers_maximum = max(numbers)  # return the largest number in a list
print(numbers_maximum)


# LIST COMPREHENSIONS (used to briefly loop over EXISTING iterables)
string_numbers = ["1", "2", "3", "4", "5"]
print(string_numbers)

float_numbers = [float(num) for num in string_numbers]  # applies a method (float) to every element of an existing list
print(float_numbers)  # the result will be stored in a new list

