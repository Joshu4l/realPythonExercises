# Introduction to WRITING to file objects:
import pathlib
my_path = pathlib.Path.cwd() / "my_folder" / "my_file.txt"
my_path.touch(exist_ok=True)



with my_path.open(mode="w", encoding="utf-8") as my_file: # notice the "w"-mode here! (we're writing here initially)

	# Now, actually write some content to the file
	# BUT: be careful, former content will be overwritten unless mode="a" is used
	my_file.write("\nHi, there")



with my_path.open(mode="a", encoding="utf-8") as my_file: # notice the "a"-mode here!

	# Now,write some more content to the file
	# BUT: This time using the "a"-mode (= "append") here
	my_file.write("\nHi, again")



# Let's check what contents we added
print("\ncontents after appending a single line of text")
with my_path.open(mode="r", encoding="utf-8") as my_file:

	for line in my_file.readlines():
		print(line, end="")





# Now, let's add SEVERAL LINES OF CONTENT using the '.writelines()' method
# Therefor, create a list of strings
lines_tba = ["\nline example 1", "\nline example 2", "\nline example 3"]  # (don't forget the new line breaks here)

with my_path.open(mode="a", encoding="utf-8") as my_file:

	# Now, applying the '.writelines()' method to our file
	my_file.writelines(lines_tba)  # takes in a list as its only argument



# Again, lets print our contents to see the results
print("\ncontents after appending a list of several lines at once")
with my_path.open(mode="r", encoding="utf-8") as my_file:

	print(my_file.read())



