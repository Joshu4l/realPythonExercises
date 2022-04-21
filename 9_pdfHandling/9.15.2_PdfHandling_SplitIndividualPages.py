# INTRODUCTION TO CROPPING PDF FILES - e.g. when we just want to cut out a certain diagram or to divide a page into TWO

# Scenario here:
# The target file is 'half_and_half.pdf' within the target folder 'practice_files'

# Issue with this document is:
# It contains an extract of Hans Christian Anderson's tale 'The Little Mermaid'
# Each page in there comes with a section of 2 columns on it.

# TASK NOW:
# Let's split each page into two pages, (one for each column) by using the '' method!

import pathlib

target_dir = pathlib.Path().cwd() / "practice_files"  # set up the directory we want to address
filepath = target_dir / "half_and_half.pdf"  # set up the filepath of the faulty file we want to work with


import PyPDF2
file_reader = PyPDF2.PdfFileReader(str(filepath))  # Instantiate a <FileReader> object using a STRING of <filepath>

# In order to crop a page:
first_page = file_reader.getPage(0)  # pick a page (in this case page 1) ...

# PLEASE NOTE: This time we will not modify the first page at the spot/right away but instead create a deepcopy
# (which we can work with without worrying about screwing sth up)
import copy
left_half = copy.deepcopy(first_page)

# now, set up a tuple for the NEW <upperRight> attribute, consisting of the following:
new_coordinates = (
	# As we are about to split a pdf along its vertical axis:
	left_half.mediaBox.upperRight[0] / 2,  # the X-coordinate shall be HALF of the actual horizontal width
	left_half.mediaBox.upperRight[1]  # the Y-coordinate (defining the height) shall remain the same
)

left_half.mediaBox.upperRight = new_coordinates  # Congrats we just cropped the first page down to only its left half

# Let's do the same thing for the right side of the page:
right_half = copy.deepcopy(first_page)
right_half.mediaBox.upperLeft = new_coordinates  # See? this time the new coordinates are used as the right half's new <upperLeft>

# Eventually, put those two separate croppings into a new <PdfFileWriter>
file_writer = PyPDF2.PdfFileWriter()
file_writer.addPage(left_half)
file_writer.addPage(right_half)

# Finally, paste the content of the <PdfFileWriter> to our result file
resultpath = target_dir / "cropped_pages.pdf"
resultpath.touch(exist_ok=True)
with resultpath.open(mode="wb") as result:
	file_writer.write(result)

fr = PyPDF2.PdfFileReader(str(resultpath))
print(fr.getNumPages())
print(fr.getPage(0).extractText())
