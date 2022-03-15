# INTRODUCTION TO PyPDF2's <PdfFileMerger> CLASS

# Most important difference between the <PdfFileWriter> and the <PdfFileMerger> is:
# The <PdfFileWriter> can only append/concatenate pages, one after another
# whereas the <PdfFileMerger> can actually INSERT pages at any given point of a document!
# Let's play around with it :)

import pathlib
import PyPDF2

pdf_merger1 = PyPDF2.PdfFileMerger()  # just like <writers>, a <merger> is instantiated WITHOUT ANY ARGUMENTS too
# So, at this point the merger is EMPTY.
# Adding pages to it can be done in 2 WAYS:


# OPTION 1:  '.append()'  simply APPENDS all pages of a document after the LAST PAGE of an existing <merger>
expense_reports_dir = (
				pathlib.Path.cwd() /
				"practice_files" /
				"expense_reports"
				)
# After setting up a directory containing 3 PDF files to practice '.append()' we put all paths in there into a list
expense_reports = sorted([path for path in expense_reports_dir.glob("*.pdf")])

for path in expense_reports:
	pdf_merger1.append(str(path))  # watch out! <Path> objects must be passed in AS A STRING

output_path = expense_reports_dir / "expense_report_appended.pdf"
with output_path.open(mode="wb") as output_file:
	pdf_merger1.write(output_file)



# Option 2:  '.merge()'  which INSERTS all pages of a document after a SPECIFIED PAGE of an existing <merger>
pdf_merger2 = PyPDF2.PdfFileMerger()

quarterly_report_dir = (
				pathlib.Path.cwd() /
				"practice_files" /
				"quarterly_report"
				)
# After setting up a directory containing 3 PDF files to practice '.merge()' we can define the paths of its files
report = quarterly_report_dir / "report.pdf"  # pdf-report of which we assume lacks a certain content (toc)
toc = quarterly_report_dir / "toc.pdf"  # pdf-content that is (for our exercise purpose) missing in the pdf-report
result_path = quarterly_report_dir / "full_report.pdf"

# initially fill our merger with the incomplete report
pdf_merger2.append(str(report))  # watch out! <Path> objects must be passed in AS A STRING

# Now, let's assume we want to insert our table of contents AFTEr the report's first (index = 0) page
# So we will merge the toc in at index 1
pdf_merger2.merge(1, str(toc))
	# fist argument is always = INDEX of the TARGET PAGE POSITION
	# second argument is always = DOCUMENT PATH (as a string) of the pdf that shall be inserted in there

# Now that we have our merger filled with the contents as we imagined them, we can actually write them to a file
with result_path.open(mode="wb") as result_file:
	pdf_merger2.write(result_file)





