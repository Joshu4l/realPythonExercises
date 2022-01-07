import pathlib

home = pathlib.Path.home()
print(f"home_path:\n - {home}\n")

new_dir = home / "new_dir"  # create a new filepath extension

print(f"new relatively extended path:\n - {new_dir}\n")
print(f"<name> component of new_dir:\n  '{new_dir.name}'\n")
print(f"<parent> component of new_dir:\n - {new_dir.parent}\n")


print("each parent-component of 'new_dir':") # from deepest folder back to root
for i in new_dir.parents:
	print(f"- {i}")

print("\n")


rel_path = pathlib.Path("/Documents/sample.txt")  # parents are complemented as far as possible but not guaranteed to appear
print(f"relative path:\n - {rel_path}\n")
print(f"relative path resolved:\n - {rel_path.resolve()}\n")


path = pathlib.Path("hello.txt")
print("components of hello.txt:")
print(f"- name       '{path.name}'")
print(f"- stem       '{path.stem}'")
print(f"- suffix     '{path.suffix}'")


print("\n")

cwd = pathlib.Path.cwd()  # pick the current working directory (=project folder) on our machine
print(f"filepath of the current working directory:\n - {cwd}\n")

filepath = cwd / "my_folder" / "my_file.txt"
print(f"constructed filepath inside the cwd:\n - {filepath}\n")
print(f"existing?   {filepath.exists()}")   # actually make a check on its existence
print(f"directory?  {filepath.is_dir()}")   # actually check if the path object is a folder
print(f"file? 	    {filepath.is_file()}")  # actually check if the path object is a file
