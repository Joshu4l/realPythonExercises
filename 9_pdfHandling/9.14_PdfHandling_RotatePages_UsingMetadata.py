# INTRODUCTION TO CROPPING AND ROTATING PDF FILES - THIS TIME: BASED ON THE METADATA OF OUR PAGE OBJECTS

# Scenario here:
# In the previous exercise we learned how to generally use the '.rotateClockwise(xy°)' method on page objects.
# But there we had to know in advance which pages were rotated in a wrong way.

# This time we're going to take advantage of the metadata each <Page> object provides naturally
# and let the program figure out the pages that need to be rotated by itself. :)

# The target file is 'ugly.pdf' within the target folder 'practice_files'


import pathlib

target_folder = pathlib.Path().cwd() / "practice_files"  # set up the directory we want to address
filepath = target_folder / "ugly.pdf"  # set up the filepath of the faulty file we want to work with

resultpath = target_folder / "rotation_result_via_metadata.pdf"  #  prepare a result filepath for when we have corrected everything
resultpath.touch(exist_ok=True)  # actually create the result file


import PyPDF2
file_reader = PyPDF2.PdfFileReader(str(filepath))  # Instantiate a <FileReader> object using a STRING of <filepath>
file_writer = PyPDF2.PdfFileWriter() # Create an empty <FileWriter> object


with resultpath.open(mode="wb") as result:  # Open our result file

	for i in range(0,file_reader.getNumPages()):  # iterate over each page of our <FileReader> object

		page = file_reader.getPage(i)  # assign each page object to a page variable one by one

		while page['/Rotate'] != 0:  # check each page's ['/Rotate'] value within its respective dictionary credentials
			page.rotateClockwise(90)  # if that value is not equal to 0, ROTATE IT UNTIL IT IS
			file_writer.addPage(page)  # finally, append that page to our <FileWriter> object

		else:
			file_writer.addPage(page)  # if the page's ['/Rotate'] value ALREADY IS equal to 0, add it as it is

	file_writer.write(result)  # Eventually paste the <FileWriter>'s contents into our result file
