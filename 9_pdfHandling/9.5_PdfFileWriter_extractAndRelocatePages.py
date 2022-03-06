# INTRODUCTION TO THE EXTRACTION OF PAGES (AND USING THEM TO CREATE A NEW PDF FILE)
# CLASS OF CHOICE FOR THAT TASK = <PdfFileWriter>

import PyPDF2
pdf_file_writer = PyPDF2.PdfFileWriter()  # no input parameters needed here!
# can be understood as a new BLANK pdf file, which has NO PAGES YET!


# In order to be able to save such thing as an actual pdf file, we need to add actual pages
new_page = pdf_file_writer.addBlankPage(width=72, height=72)  # 1 measurement-point equals 1/72 of an inch
print(type(new_page))
# Background information: <PdfFileWriter> objects can write to new PDF files, BUT
# they cannot create new content from scratch other than blank pages


import pathlib
output_file_path = pathlib.Path.cwd() / "practice_files" / "blank.pdf"
output_file_path.touch(exist_ok=True)

# SPECIAL SYNTAX FOR THIS KIND OF OPERATION:
with output_file_path.open(mode="wb") as output_file:  # handling pdf requires the write-mode to be BINARY!

	# Other than usually, we do  NOT  pass the <pdf_file_writer> to the output file's  '.write' method, but vice versa!
	pdf_file_writer.write(output_file)
	# Instead, the OUTPUT FILE ITSELF BECOMES A PARAMETER for the <pdf_file_writer> object
	# Like saying "I want to write/create a new pdf...
	# ...and where I want that new content to be stored, is located under the path of <output_file_writer> "


# CONCLUSION of what is necessary to create a new PDF file:

# 1st step:  Create a <PdfFileWriter> instance
# 2nd step:  Add one or more pages to the <PdfFileWriter> instance
# 3rd step:  Pass a new file location to the <PdfFileWriter>'s  '.write()'-method

