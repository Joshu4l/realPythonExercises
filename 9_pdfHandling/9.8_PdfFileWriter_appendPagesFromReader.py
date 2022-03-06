# INTRODUCTION TO PyPDF2's  '.appendPagesFromReader'  method
import PyPDF2

# USEFUL HACK:
# Sometimes you need to extract EVERY page from a PDF. That can of course be done by the methods we explored earlier
# (like nesting '.addPage' into a for loop), BUT PyPDF2 comes with a shortcut for that! :)
# <PdfFileReader> instances have a '.appendPagesFromReader' method that can be used to append pages from a <PdfFileReader> instance directly:

# Works like the following example
import pathlib

example_path = pathlib.Path.cwd() / "practice_files" / "Pride_and_Prejudice.pdf"
pdf_file_reader = PyPDF2.PdfFileReader(str(example_path))

pdf_file_writer = PyPDF2.PdfFileWriter()
pdf_file_writer.appendPagesFromReader(pdf_file_reader)  # simple as that, no loop needed!
# We're simply providing a <PdfFileReader> instance as an argument here and everything will be copied!


# From there on we could continue and paste that file writer content into a new file e.g.:
target_path = pathlib.Path.cwd() / "practice_files" / "Pride_and_Prejudice_complete_copy.pdf"
target_path.touch(exist_ok=True)

with target_path.open(mode="wb") as target:
	pdf_file_writer.write(target)

print("done")

