# INTRODUCTION TO READING AND WRITING CSV FILES (that are more complex = mixed data with respective headers)
import pathlib
import csv

practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "employees.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)


first_content = [
				["name","department","salary"],
				["Lee","Operations",75000.00],
				["Jane","Engineering",85000.00],
				["Diego","Sales",80000.00]
				]

with filepath.open(mode="w", encoding="utf-8", newline="") as file:
	writer_obj = csv.writer(file)
	writer_obj.writerows(first_content)


# normally we would read the file's content like this:
with filepath.open(mode="r", encoding="utf-8", newline="") as file:
	reader_obj = csv.reader(file)
	for i in reader_obj:
		print(i)


# now that we're dealing with mixed data and corresponding headers,
# we can proceed with the csv module's '.DictReader'-method:
with filepath.open(mode="r", encoding="utf-8", newline="") as file:

	# it takes in an opened file as its only argument and works like a normal dict from there on!
	dictReader_obj = csv.DictReader(file)

	# example for getting the table headers
	print(f"\nfield names of the DictReader object: {dictReader_obj.fieldnames}")

	# example for getting the table values
	print(f"\nkey value pairs of the DictReader object:")
	for entry in dictReader_obj:
		print(entry)

	# IMPORTANT THING TO KNOW:
	# The for-loop above runs over the entire file content, BUT
	# As soon as it is done with that, it will assume there is nothing more to do here using the dictReader_obj!
	# In other words: DictReader objects are NOT reusable automatically
	# So, in order make the DictReader reusable (to loop over as often as we want), we have two options here:

	# OPTION 1: set the viewed section of our file back to the start (every time) manually
	file.seek(0)  # this causes the imaginary 'cursor' jump back to the starting position of the file
	print("\n")
	for entry in dictReader_obj:
		print(entry)

# OPTION 2: turn the dictReader object into a list (which  is mutable)
with filepath.open(mode="r", encoding="utf-8", newline="") as file:
	dictReader_obj = csv.DictReader(file)
	dictReader_obj_reusable = list(dictReader_obj)

	print("\nnow that we turned the DictReader object into a list, we can reuse it:\nusage demo 1:")
	for i in dictReader_obj_reusable:
		print(i)

	print("\nnow that we turned the DictReader object into a list, we can reuse it:\nusage demo 2:")
	for i in dictReader_obj_reusable:
		print(i)

