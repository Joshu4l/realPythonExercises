# DEEP COPIES:
# (USED TO NOT ONLY REFERENCE A LIST BUT TO ACTUALLY COPY IT WITH ALL ITS OBJECTS!)

# pythons copy module
import copy
from copy import deepcopy


# creating a 2-dimensional list again
matrix_original = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# this time copying it by using the deepcopy function from pythons copy-module
matrix_copy = deepcopy(matrix_original)

print(matrix_original)
print(matrix_copy)


# Now try to change a 2nd level element of the copy without altering our original
matrix_copy[0][0] = "X"


# Show the original to make sure it didn't change
print(f"{matrix_original} -> Great, nothing changed here! :)")
# Show our deep copy to check for its current state
print(f"{matrix_copy} -> Yep, there's the edit we made! :)")




