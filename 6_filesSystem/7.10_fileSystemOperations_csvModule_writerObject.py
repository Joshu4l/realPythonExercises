#

import pathlib
import csv

practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "new_file.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)

# prepare some data to write to our file
daily_temperatures = [ [68,65,68,70,74,72],
					   [67,67,70,72,72,70],
					   [68,70,74,76,74,73]
					   ]


# this time instead of using a with statement we'll assign the opened file to a variable <file> right away
with filepath.open(mode="w", encoding="utf-8", newline="") as file:  # newline="" makes sure we won't add unwanted blank lines

	writer_obj = csv.writer(file)  # produces a <csv.writer-OBJECT> which has its own useful csv write-methods in store!
	# now given that special kind of object the main advantage is:
	# we don't need to convert our list values into strings before being able to write to the file!
	# the csv.writer-object handles that by itself. :)

	# now we got two writing-possibilities to choose from:

	# 1. either looping over a list and tell the writer_obj to '.writerow' each sub-item separately
	for temp_vals in daily_temperatures:
		writer_obj.writerow(temp_vals)

	# 2. or using '.writerowS' right away and pass a list of lists as the only argument
	# ATTENTION: here, on the first level of that input list, ONLY ITERABLES ARE ALLOWED (str's are okay, int's are NOT)
	writer_obj.writerows(daily_temperatures)



