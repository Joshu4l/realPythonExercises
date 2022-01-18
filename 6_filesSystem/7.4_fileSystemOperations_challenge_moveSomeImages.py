# For this exercise, a directory called <practice_files> shall contain a subfolder called <documents/>.
# This subfolder itself also contains several files and subfolders.
# Some of the files are images ending with the .png, .gif or .jpg file extension.

# Create a new folder in the <practice_files> folder called <images/>, and move all image fieles to that folder.
# When you're done, the new folder should have four files in it:
# 1. image1.png
# 2. image2.gif
# 3. image3.png
# 4. image4.jpg

import pathlib

docs = pathlib.Path.cwd() / "practice_files" / "documents"

images = pathlib.Path.cwd() / "practice_files" / "images"
images.mkdir(parents=True, exist_ok=True)

# search for all contents (including subfolders) in the 'documents'-directory...
# ...which are ending with one of the targeted suffixes
for i in docs.rglob("*[.png, .gif, .jpg]"):

	# then change the path for each of those resulting files
	i.replace(images / i.name)

print("all targeted files have been shifted")
