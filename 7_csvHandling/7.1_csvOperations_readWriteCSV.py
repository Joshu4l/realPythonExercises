# Introduction on how to read and write csv data
import pathlib
# First, create a target csv file
file_path = pathlib.Path.cwd() / "practice_files" / "temperatures.csv"
file_path.touch(exist_ok=True)
print(file_path.is_file())
print(file_path.exists())


temperature_readings = [68, 65, 68, 70, 74, 72]


# open the file in APPEND mode
with file_path.open(mode="a", encoding="utf-8") as file:  # for demonstration only using "w"-mode here

	# 1. tell the file to write lines
	# 2. provide an f-string
	# 3. declare that behind every existing line of the file a line-break is added
	# 4. turn each element of a given list into a string character and concatenate them via commas
	file.writelines(f"\n{ ','.join( str(r) for r in temperature_readings ) }")



with file_path.open(mode="r", encoding="utf-8") as file:

	# Let's be creative: set up three kinds of containers:

	# one for a concatenated string
	concat_content = [line.strip("\n") for line in file.readlines()]
	for i in concat_content:
		print(type(i), i) 	# proof the type of content here


	# one for a list of string-element-sublists
	string_container = [line.split(",") for line in concat_content]
	print(string_container)  # proof the type of content for this one too


	# and one for a list of integer values (AS FAR AS THE GIVEN LIST-VALUES ALLOW IT!)
	num_container = []
	for string_sublist in string_container:
		num_sublist = []

		for item in string_sublist:

			try:
				item = int(item)
				num_sublist.append(item)
			except ValueError: # handles cases where we attempt to turn a word into an integer
				continue

		if num_sublist:
			num_container.append(num_sublist)  # make sure only non-empty lists are appended
		else:
			continue


	print(num_container) # proof numeric sublists were only created if the value could be turned into an integer

