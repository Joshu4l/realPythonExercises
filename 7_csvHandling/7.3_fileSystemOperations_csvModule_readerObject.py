# INTRODUCTION TO THE CSV MODULE'S '.reader' OBJECT

import pathlib
import csv

practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "new_file.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)


# 1/2
with filepath.open(mode="r", encoding="utf-8", newline="") as file:  # newline="" makes sure we won't add unwanted blank lines

	reader_obj = csv.reader(file)  # produces a <csv.reader-OBJECT> which has its own useful csv read-methods in store!
	# now that we instantiated a reader object from our file object, we're provided with two reading-possibilities:

	# possibility 1/2: simply iterate over each row and read their values as lists of strings
	for row in reader_obj:
		print(row)


# 2/2
with filepath.open(mode="r", encoding="utf-8",newline="") as file:  # newline="" makes sure we won't add unwanted blank lines

	reader_obj = csv.reader(file)  # produces a <csv.reader-OBJECT> which has its own useful csv read-methods in store!
	# now that we instantiated a reader object from our file object, we're provided with two reading-possibilities:

	# possibility 2/2: use a list comprehension in order to actually restore numeric values
	daily_temperatures_restored = []
	for row in reader_obj:
		int_row = [int(val) for val in row]
		daily_temperatures_restored.append(int_row)

	print(daily_temperatures_restored)
