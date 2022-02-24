# INTRODUCTION TO READING AND WRITING CSV FILES (that are more complex = mixed data with respective headers)
import pathlib
import csv

practice_dir = pathlib.Path().cwd() / "practice_files"

filepath = practice_dir / "employees.csv"
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch(exist_ok=True)


with filepath.open(mode="r", encoding="utf-8", newline="") as file:

	dictReader_obj = csv.DictReader(file)  # set up a DictReader object for the csv file
	dictReader_obj_reusable = list(dictReader_obj)  # turn the DictReader object into a list (for reuseability)

	print("\nDict contents without any transformations:")
	for i in dictReader_obj_reusable:
		print(i)  # note that even numeric values will be returned as strings this way

	# we can avoid that by writing a function that turns all possible values into a float
	def transform_numerics(dict_list):
		"""turns string-numbers of a DictReader object into actual numerics"""
		for sub_dict in dict_list:
			for key, value in sub_dict.items():
				try:
					sub_dict[key] = float(value)
				except ValueError:
					continue
		return dict_list


# proof that we managed to transform the salary values into floats (instead of strings)
transform_numerics(dictReader_obj_reusable)
print("\nDict contents after transforming the salary types:")
for i in dictReader_obj_reusable:
	print(i)




