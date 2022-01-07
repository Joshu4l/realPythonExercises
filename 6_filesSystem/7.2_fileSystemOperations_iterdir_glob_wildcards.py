# these exercises are using the files and directories which were
# created via module <7.1_fileSystemOperations_mkdir_touch>

import pathlib
cwd = pathlib.Path.cwd()
new_directory = cwd / "new_directory"


# how iterating through a directory via a for-loop and 'ITERDIR' generally works:
# (subdirectory contents are NOT included! in this procedure)
for i in new_directory.iterdir():
	# do something
	pass

# wrapping a directory-iteration into a function
def show_contents(target_directory):
	""".iterdir() returns all path objects in a specified directory"""

	if target_directory.is_dir():
		for pathobject in target_directory.iterdir():
			print(pathobject)
	else:
		print("the path that was specified is not a directory. Thus, no contents possible to be returned!")

# call the 'show_contents'-function on our new_directory
show_contents(new_directory)
# demonstrate what happens when attempting to show_contents of a file
show_contents(pathlib.Path(r"/new_directory/program1.py"))
print("\n")



# how searching for a specific content name via a for loop and 'GLOB' generally works:
for i in new_directory.glob("*file*"):
	# do something
	pass

# wrapping a directory-search into a function
def search_content(search_term, target_directory):
	"""returns all path object contents within a specified directory for a specified search term"""

	print(f"contents for your search term '{search_term}':")
	for content in target_directory.glob(f"*{search_term}*"):

		if content.is_dir():
			content_type = '<Directory>'
		else:
			content_type = '<File>'
		print(f"- type of content: {content_type},  stem: '{content.stem}',  suffix: {content.suffix}")

# call the 'show_contents'-function on our new_directory
search_content("file", new_directory)
print("\n")



# working with 'GLOB' in combination with WILDCARDS (such as '*', '?' and '[]'):
#
# The '?'-wildcard
print("contents for your search term 'program?.py':")
for i in new_directory.glob("program?.py"): # note that '?' replaces exactly 1 character
	print(f"- {i}")
print("\n")

# The '*'-wildcard
print("contents for your search term '*.txt':")
for i in new_directory.glob("*.txt"): # note that '?' replaces exactly 1 character
	print(f"- {i}")
print("\n")

# The '[]'-wildcard
print("contents for your search term '*[.py,.txt]':")
for i in new_directory.glob("*[.py,.txt]"): # note that '[]' accepts whatever argument turns out to be found
	print(f"- {i}")
print("\n")



# GLOB-ing INCLUDING SUBDIRECTORIES!
#
# Recursive Matching with the '**' Wildcard
def search_content_recursive(search_term, target_directory):
	"""returns all matching contents of a directory - INCLUDING ALL ITS SUBDIRECTORIES - for a specified search term"""

	print(f"contents for your search term '{search_term}':")
	for content in target_directory.glob(f"**/{search_term}"):

		if content.is_dir():
			content_type = '<Directory>'
		else:
			content_type = '<File>'
		print(f"- type of content: {content_type},  stem: '{content.stem}',  suffix: {content.suffix}")
		print(f"  location: {content.parent}")

# call the 'show_contents_recursive'-function on our new_directory
search_content_recursive("*.txt", new_directory)
print("\n")



# BUT! SHORTCUT VERSION of using  '**/'  is -->  using 'RGLOB'
print(r"example for using 'rglob(*.txt)' as a smarter substitution of '.glob(**/*.txt)' ")
for result in new_directory.rglob("*.txt"):
	print(f"- {result}")


