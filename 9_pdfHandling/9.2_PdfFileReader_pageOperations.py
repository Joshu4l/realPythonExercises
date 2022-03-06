import pathlib
from PyPDF2 import PdfFileReader

# Set up the path to our pdf practice file
pdf_source_path = (pathlib.Path.cwd() /
				   "practice_files" /
				   "Pride_and_Prejudice.pdf"
				   )

# Now, actually create a <PdfFileReader> instance
pdf = PdfFileReader(str(pdf_source_path))
print(type(pdf))


# Let's extract some text from the PdfFileReader instance we just created above
# THIS ALWAYS MEANS 2 STEPS:

# 1. Get a <PageObject> out of our <PdfFileReader> object
page1 = pdf.getPage(0)
print(type(page1))

# 2. Actually extract text from the page object(s) we chose above
page1_content = page1.extractText()
print(page1_content)


# Works also with for-loops, allowing to iterate over each page of the document
# Would look like this:
# for p in pdf.pages():
# 	print(p.extractText())


