# INTRODUCTION TO CROPPING PDF FILES - e.g. when we just want to cut out a certain diagram or to divide a page into TWO

# Scenario here:
# The target file is 'half_and_half.pdf' within the target folder 'practice_files'

# Issue with this document is:
# It contains an extract of Hans Christian Anderson's tale 'The Little Mermaid'
# Each page in there comes with a section of 2 columns on it.

# TASK NOW:
# Let's split each page into two pages, (one for each column) by using the '' method!

import pathlib

target_folder = pathlib.Path().cwd() / "practice_files"  # set up the directory we want to address
filepath = target_folder / "half_and_half.pdf"  # set up the filepath of the faulty file we want to work with


import PyPDF2
file_reader = PyPDF2.PdfFileReader(str(filepath))  # Instantiate a <FileReader> object using a STRING of <filepath>

# In order to crop a page:
first_page = file_reader.getPage(0)  # pick a page (in this case page 1) ...

print(first_page.mediaBox)  # ... and inspect its 'mediaBox' properties, so we get a <rectangleObject> returned
	# Output RectangleObject([0, 0, 792, 612]) explained:
	# first two numbers  0 and 0  representing the x and y coordinates of the lower left corner of the rectangle
	# second two numbers 792 and 612 representing the width and height of the rectangle respectively

# Let's access the ATTRIBUTES OF THE MEDIABOX-RECTANGLE:
print(f"lower left corner coordinates:  {first_page.mediaBox.lowerLeft}")
print(f"lower right corner coordinates: {first_page.mediaBox.lowerLeft}")

print(f"upper left corner coordinates:  {first_page.mediaBox.upperLeft}")
print(f"upper right corner coordinates: {first_page.mediaBox.upperRight}")
# each attribute returns a tuple of two coordinate values of the respective corner


# We can alter/reassign the values of the corners, e.g.
first_page.mediaBox.upperLeft = (0, 480)
print(first_page.mediaBox.upperLeft)
# (in order to maintain its rectangular shape) <upperRight> will adjust to the Y-coordinate of <upperLeft> automatically
print(first_page.mediaBox.upperRight)


# At this point we already actually cropped a page by altering its default measurements
# Let's put that result into a FileWriter and save it:

file_writer = PyPDF2.PdfFileWriter()  # Create an empty <FileWriter> object
file_writer.addPage(first_page)

resultpath = target_folder / "cropped_page.pdf"  #  prepare a result filepath for when we have corrected everything
resultpath.touch(exist_ok=True)  # actually create the result file

with resultpath.open(mode="wb") as result:
	file_writer.write(result)
