# 1. Write the following text to a file called 'starships.txt' in your 'practice_files' directory:

#    Discovery
#    Enterprise
#    Defiant
#    Voyager

# Each word should be on a separate line

words_to_add = "Discovery\n, Enterprise\n, Defiant\n, Voyager\n"
starships = words_to_add.split(", ")  # set up a list here

import pathlib
filepath = pathlib.Path.cwd() / "practice_files" / "starships.txt"
filepath.touch(exist_ok=True)  # create the necessary file here

with filepath.open(mode="w",encoding="utf-8") as file:
	file.writelines(starships)  # actually write to the file (using our list) here




# 2. Read the file 'starships.txt' that you created in step 1 and print each line of text in the file.
# The output should not have extra blank lines between each word.

with filepath.open(mode="r", encoding="utf-8") as file:

	for line in file.readlines():
		print(line, end="")  # actually read each line of the file (while ignoring blank lines) here

