# INTRODUCTION TO READING AND WRITING CSV FILES (that are more complex = mixed data with respective headers)
import pathlib
import csv

practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "employees.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)


first_content = [["name,department,salary"],
				 ["Lee","Operations",75,000.00],
				 ["Jane","Engineering",85,000.00],
				 ["Diego","Sales",80,000.00]
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
# we can proceed with the csv module's ''-method:

