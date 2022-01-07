# Setting up an empty DICTIONARY first:
cats = {}

# Filling in one-hundred ascending dictionary keys
for i in range(1, 101):
    cats[i] = 'no hat'  # respectively with the initial default-value: "no hat"

# importing python's json-module in order to print dictionaries in a more structured format
import json
print(json.dumps(cats, sort_keys=True, indent=4))


# creating an empty LIST
cats_list = []

# filling the empty cat list with the respective cat-kvp's
for key, value in cats.items():
    cats_list.append([key, value])


# creating a STEP-parameter (which means the n'th element of a container)
n = 1

# each loop, increase the cat-index which we're starting from
for starting_index in range(100):

    # loop over  EVERY N'TH CAT-KVP  in our cats list
    for cat in cats_list[starting_index::n]:

        # for each of those cat-kvp's, check the 'hat'-value
        if cat[1] == 'no hat':
            cat[1] = 'hat'

        else:
            cat[1] = 'no hat'

    # each loop, increment the step-parameter by one
    n = n + 1


# finally, print only those cats which actually have a hat on by now
for c in cats_list:
    if c[1] == 'hat':
        print(c)

