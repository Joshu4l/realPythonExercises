# MOVING files or directories via the '.replace(<new_path>)' method:
import pathlib

# Define a target file to apply these actions on
cwd = pathlib.Path().cwd()
source = cwd / "new_directory" / "source.txt"
source.touch(exist_ok=True)



# Define a new path for the destination folder (That's where the file shall land)
destination_dir = cwd / "new_directory" / "destination_folder"
destination_dir.mkdir(parents=True, exist_ok=True)

# Define a new path for the destination FILE
destination_file = destination_dir / "destination.txt"

# Now, actually MOVE the 'source'-file using the '.replace(<new_path>)' method
if not destination_file.exists():
	source.replace(destination_file)  # IMPORTANT:
	# ALWAYS, ALWAYS make sure the destination does not already exist!
	# Otherwise, the prior data there will be deleted irreversible
else:
	print("file was not moved! The target path object already exists.")




# DELETING FILES using the '.unlink()' method:

# Define a new path for a target file to be deleted
to_be_deleted_file = cwd / "new_directory" / "to_be_deleted.txt"
to_be_deleted_file.touch(exist_ok=True)

# Now, actually DELETE the 'to_be_deleted_file' using the '.unlink()' method (works only with FILE objects)
# can be understood as a counterpart to <.touch()>
to_be_deleted_file.unlink(missing_ok=True)
	# Note: the 'missing_ok=True' attribute makes sure, no error is raised if
	# the file supposed to be deleted does not even exist. :)


# DELETING EMPTY DIRECTORIES using the '.rmdir(<targeted_dir>)' method
to_be_deleted_dir = cwd / "new_directory" / "to_be_deleted"
to_be_deleted_dir.mkdir(parents=True, exist_ok=True)

# Now, actually DELETE the 'to_be_deleted' directory using the '.rmdir()' method
# can be understood as a counterpart to <.mkdir()>
to_be_deleted_dir.rmdir()
	# Note: the .rmdir() method only works for directories that are EMPTY!
	# In order to delete a whole tree it's necessary to use a method from the 3rd party lib 'SHUTIL'



# DELETING A DIRECTORY INCLUDING ALL ITS CONTENTS using the shutil's '.rmtree()' method
import shutil

# create a directory
to_be_deleted_tree = cwd / "new_directory" / "to_be_deleted_tree"
to_be_deleted_tree.mkdir(parents=True, exist_ok=True)

# create some content
bla1 = to_be_deleted_tree / "bla1.txt"
bla1.touch(exist_ok=True)
bla2 = to_be_deleted_tree / "bla2.txt"
bla2.touch(exist_ok=True)
bla3 = to_be_deleted_tree / "bla3.txt"
bla3.touch(exist_ok=True)

# Now, actually DELETE the directory and all its contents using 'shutil.rmtree(<targeted_folder>)'
shutil.rmtree(to_be_deleted_tree)