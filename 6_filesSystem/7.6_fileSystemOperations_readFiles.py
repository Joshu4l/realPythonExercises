# Introduction to reading of and writing into file objects:

import pathlib

my_path = pathlib.Path.cwd() / "my_folder" / "my_file.txt"
my_path.touch(exist_ok=True)

with my_path.open(mode="r", encoding="utf-8") as my_file:

	# using the '.read()' method, we can access the file's actual (utf-8-encoded) content
	content = my_file.read()

	print(type(content)) # show what kind of data we're even dealing with
	print(content) #  show the actual content

	my_file.close()



with my_path.open(mode="r", encoding="utf-8") as my_file:

	# instead of reading everything at once
	# use the '.readlines()' method to iterate over each row
	print("\nprinted line by line")

	for l in my_file.readlines():
		print(l, end="")  # setting the <end> attribute to ="" causes the iterator to skip blank lines

	my_file.close()




