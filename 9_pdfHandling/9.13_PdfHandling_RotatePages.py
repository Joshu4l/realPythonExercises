# INTRODUCTION TO CROPPING AND ROTATING PDF FILES

# Scenario to begin:
# The target file is 'ugly.pdf' within the target folder 'practice_files'
# EVERY ODD PAGE is rotated 90° COUNTERCLOCKWISE. Let's solve this by rotating the pages back in their correct angles.

import pathlib

target_folder = pathlib.Path().cwd() / "practice_files"  # set up the directory we want to address
filepath = target_folder / "ugly.pdf"  # set up the filepath of the faulty file we want to work with

resultpath = target_folder / "rotation_result.pdf"  #  prepare a result filepath for when we have corrected everything
resultpath.touch(exist_ok=True)  # actually create the result file


import PyPDF2
file_reader = PyPDF2.PdfFileReader(str(filepath))  # Instantiate a <FileReader> object using a string of <filepath>
file_writer = PyPDF2.PdfFileWriter() # Create an empty <FileWriter> object

for page in range(0,file_reader.getNumPages(),2): # pick out every second page (step = 2) of our <FileReader>, starting at index 0
	file_reader.getPage(page).rotateClockwise(90) # rotate those pages clockwise by 90 degrees


with resultpath.open(mode="wb")	as result:  # open our result filepath

	for rotated_page in range(file_reader.getNumPages()): # pick out EVERY page from our (now correct) <FileReader>

		rotated_page = file_reader.getPage(rotated_page)
		file_writer.addPage(rotated_page)  # put those pages into our <FileWriter> object

	file_writer.write(result)  # FINALLY paste our <FileWriter> contents into our result file


