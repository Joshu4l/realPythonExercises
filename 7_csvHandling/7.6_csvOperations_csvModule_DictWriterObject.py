# INTRODUCTION TO WRITING CSV FILES (using the csv.DictWriter)
import pathlib
import csv
practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "people.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)


people_data = [
	{"name": "Veronica", "age": 29},
	{"name": "Audrey", "age": 32},
	{"name": "Sam", "age": 24},
	]


# normal way of opening the targeted file in "write"-mode
with filepath.open(mode="w", encoding="utf-8", newline="") as file:

	# THIS TIME	we will use a DictWRITER instead of a DictReader object
	# What is special here is --> we need provide a <fieldnames> parameter

	# Option 1:
	# dictWriter_obj = csv.DictWriter(file, fieldnames=["name", "age"])

	# Option 2:
	# In case the input dict keys are unknown or when list literals are impractical, it would also work like this
	people_headers = [key for key in people_data[0].keys()]
	dictWriter_obj = csv.DictWriter(file, fieldnames=people_headers)

	dictWriter_obj.writeheader()  # makes use of our previous <fieldnames>-definition and inserts them via this method
	dictWriter_obj.writerows(people_data)  # takes in several dicts as arguments and uses their values to actually write data


