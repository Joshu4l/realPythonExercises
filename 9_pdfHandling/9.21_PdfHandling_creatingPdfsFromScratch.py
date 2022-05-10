# INTRODUCTION TO: CREATING PDF FILES FROM SCRATCH
# Here, we're going to use another library than before:  The 'ReportLab Toolkit'

# Reason/Advantage of 'Reportlab Toolkit' over 'PyPDF2' is:
# PyPDF2 is great for reading and modifying Pdfs but lacks functionalities for creating them from scratch!
# So, let's dive right in and see what we can do with the new lib:


# Important to know here: the main interface for creating PDFs is the 'Canvas'-class which is located as follows
from reportlab.pdfgen.canvas import Canvas

# It is instantiated by providing a string of the intended file name, e.g.:
my_canvas = Canvas("hello.pdf")

# In order to add some text to our <Canvas> instance, we can use its 'drawString()' method:
my_canvas.drawString(72, 72, "Hello, World!")
	# argument1 = coordinate on the x-axis (value is measured in 'points', whereas 1 point = 1/72 inches)
	# argument2 = coordinate on the y-axis (value is measured in 'points', whereas 1 point = 1/72 inches)
	# argument3 = the text we want to add (with the first letter starting the position of our x/y-coordinates

# Finally, in order to save that state of the document we can use the '.save()' method:
my_canvas.save()  # can be thought of as the Canvas class's '.touch()'

