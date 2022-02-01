# Introduction to FILE OBJECTS:


# 1st possibility of creating and accessing a file object using 'open(<specific path-string>)'

# This way of using 'open()' doesn't require using a pathlib setup in between, it can be introduced right away
my_file = open(r'C:\\Users\Joshua Albert\PycharmProjects\realPythonExercises\6_filesSystem\my_folder\my_file.txt', mode="r", encoding="utf-8")
# possible options for the mode-parameter:
# "r" = read
# "w" = write
# "a" = append content

# possible options for the character encoding-parameter:
# "utf-8"
# "utf-16"
# "utf-32"
# "ascii"
print(my_file)



# 2nd possibility of creating and accessing a file object using '.open()'
# (requires an existing path object)
import pathlib

my_filepath = pathlib.Path.cwd() / "my_folder" / "my_file.txt"  # At first, set up a filePATH for a specific file

# Now, using 'with ... as <my_file>:' we make sure the file resources in memory are cleaned up after usage
# '.open()' causes python to actually INSTANTIATE a fileOBJECT

with my_filepath.open(mode="r", encoding="utf-8") as my_file:
	something = 5

# possible options for the mode-parameter:
# "r" = read
# "w" = write
# "a" = append content

# possible options for the character encoding-parameter:
# "utf-8"
# "utf-16"
# "utf-32"
# "ascii"
print(my_file)  # the output will show that we created an object belonging to class <_io.TextIOWrapper>

# Always close the file again so there won't be remainders in memory
my_file.close()