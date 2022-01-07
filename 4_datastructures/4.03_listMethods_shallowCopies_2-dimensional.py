# TWO-DIMENSIONAL SHALLOW COPIES of lists:


# COPYING A 2-DIMENSIONAL LIST:  USING THE 'SLICE ALL' METHOD
original = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(f"Original:               {original}")


# Create the copy by taking the entire slice of 'original'
copy_from_slicing = original[:]  # important: doesn't work without typing slice-brackets
print(f"Copy from slicing:      {copy_from_slicing}")


# Edit the !COPY! and check the behaviour of the ORIGINAL
copy_from_slicing[0][0] = "edit done to COPY"
print(f"ORIGINAL after renaming the [0][0]-element of COPY to 'edit done to COPY':      {original} -> see? despite not touching the original it is still altered!")


# Edit the !ORIGINAL! and check the behaviour of the COPY
original[1][4] = "edit done to the ORIGINAL"
print(f"COPY after renaming the [1][4]-element of ORIGINAL to 'edit done to ORIGINAL':  {copy_from_slicing} -> see? despite not touching the copy it is still altered!")


# CONCLUSIONS:
# USING SLICING TO COPY A 2-DIMENSIONAL LIST RESTRICTS OUR POSSIBILITIES OF ALTERING OUR LISTS INDEPENDENTLY
# THAT'S BECAUSE [:] IS REALLY JUST A REFERENCE TO ELEMENTS OF 'ORIGINAL', BUT NOT EQUAL TO  ACTUAL   O B J E C T S

# 'SLICED' COPIES CAN BE THOUGHT OF LIKE A COLLECTION OF BOOKMARKS POINTING TO THE 'ORIGINAL'-RESOURCES
# THIS IS THE REASON WHY YOU CAN DO INDEPENDENT CHANGES ON FIRST LEVEL ELEMENTS BUT NOT ON DEEPER ELEMENTS:

#      FIRST LEVEL CHANGES ARE SIMILAR TO 'RENAMING YOUR BOOKMARK' (or adding further ones)
#      SECOND LEVEL CHANGES ARE SIMILAR TO 'TRYING TO CHANGE THE ACTUAL RESOURCE': THIS WILL REFLECT ON THE ORIGINAL!!


# BUT STILL:
# ALTERING THE COPY ON ITS FIRST DIMENSION STILL WORKS FINE WITHOUT HAVING THE ORIGINAL CHANGED AGAIN TOO.
copy_from_slicing.append([11])
print(f"{original}       -> see? 1st-level-changes to 'COPY' DON'T affect our 'ORIGINAL' list")
print(f"{copy_from_slicing} -> see? 1st-level changes to 'COPY' were indeed possible without affecting the 'ORIGINAL' list ")


