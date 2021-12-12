# ONE-DIMENSIONAL SHALLOW COPIES of lists:


# COPYING A 1-DIMENSIONAL LIST:  USING THE 'SLICE ALL' METHOD
original = [1, 2, 3, 4, 5]
print(f"Original:               {original}")


# Create the copy by taking the entire slice of 'original'
copy_from_slicing = original[:]  # important: doesn't work without typing slice-brackets
print(f"Copy from slicing:      {copy_from_slicing}")


# Edit the !COPY! and check the behaviour of the ORIGINAL
copy_from_slicing[0] = 7
print(f"ORIGINAL after setting the first element of COPY to '7':  {original} -> see, the original was not affected by the change!")


# Edit the !ORIGINAL! and check the behaviour the COPY
original[0] = 0
print(f"COPY after setting the first element of ORIGINAL to '0':  {copy_from_slicing} -> see, the copy was not affected by the change!")


# CONCLUSIONS:
# USING SLICING TO COPY A 1-DIMENSIONAL LIST REPRESENTS ONLY A SNAPSHOT OF THAT VERY MOMENT
# THIS IS CALLED A 'SHALLOW COPY'
# THAT MEANS, ALTERING THE SHALLOW COPY AFTER CREATING IT WON'T APPLY ANY CHANGES TO THE ORIGINAL LIST AND VICE VERSA


# Similarly, APPENDING elements to the original DOESN'T mean that they will also be added to the copy
original.append(6)
print(f"ORIGINAL after appending '6':         {original} -> we see that 6 was appended.")
print(f"COPY after '6' was added to ORIGINAL: {copy_from_slicing} -> see, the copy stays unaffected again!")
