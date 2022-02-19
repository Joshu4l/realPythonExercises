import pathlib
cwd = pathlib.Path.cwd()

# after setting up a new path object...
new_directory  = cwd / "new_directory"

# ... now actually CREATE the corresponding directory
new_directory.mkdir(parents=True, exist_ok=True)
# 'parents=True' means:	also create all necessary upstream parents
# 'exist_ok=True' means: only create the directory if it doesn't already exist
print(new_directory.exists())

# using <MKDIR>, create a new subdirectory (b) including one missing parent ('folder_a') in between
folder_b = new_directory / "folder_a" / "folder_b"
folder_b.mkdir(parents=True, exist_ok=True)

# using <TOUCH>, it is possible to actually CREATE A FILE
image1 = folder_b / "image1.jpg"
image1.touch(exist_ok=True)  # note that touch() also has an <exist_ok> method which is set to True by default!
image2 = folder_b / "image2.png"
image2.touch()
program3 = new_directory / "folder_a" / "program3.py"
program3.touch()

# create some more stuff (directories as well as files)
folder_c = new_directory / "folder_c"
folder_c.mkdir(parents=True, exist_ok=True)
file2 = new_directory / "folder_c" / "file2.txt"
file2.touch()
file1 = new_directory / "file1.txt"
file1.touch()
program1 = new_directory / "program1.py"
program1.touch()
program2 = new_directory / "program2.py"
program2.touch()


