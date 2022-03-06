import pathlib
from PyPDF2 import PdfFileReader

# Set up the path to our pdf practice file
pdf_source_path = (pathlib.Path.cwd() /
				   "practice_files" /
				   "Pride_and_Prejudice.pdf"
				   )

# Now, actually create a <PdfFileReader> instance
pdf = PdfFileReader(str(pdf_source_path))
	# NOTE: pdf is a complex format,
	# AND: the PdfFileReader does not know how to read from a pathlib object
	# So, we need to initialize it as a STRING!

# Now that we have stored the <PdfFileReader> -object into a variable,
# We can perform some operations on it:

# Find out with what kind of object we're dealing with
print(type(pdf))

# Get the number of pages of the document
print(pdf.getNumPages())

# Get some metadata of the document
print(pdf.documentInfo)

# Each attribute of this document information can be accessed by concatenating it to the documentInfo
print(pdf.documentInfo.title)

# Also, the document information is iterable
for key, attribute in pdf.documentInfo.items():
	print(f"{key}: {attribute}")

