from reportlab.pdfgen.canvas import Canvas

# Some information about the defaults that are automatically set when using '.save()':
# Default page size:  the Canvas class automatically uses DIN A4 as its default page size
# Default font size:  the Canvas class automatically uses 'Helvetica' with a font size of 12 points

# We don't necessarily need to keep these settings mentioned above.
# E.g. in order to change the page size we can provide a 'pagesize=()' parameter (which is a tuple of two values)
my_other_canvas = Canvas("hello again.pdf", pagesize=(612, 792)) # here we create an 8.5 by 11.0 inches page
# In this case we do not actually '.save()' it but this would be how it would be defined

# For doing the annoying recalculations between inches and centimeters, the reportlab lib comes with a dedicated module:
from reportlab.lib.units import inch, cm
print(inch) # shows: how many 'points' an inch consists of
print(cm)   # shows: how many 'points' a centimeter consists of

my_unit_canvas = Canvas("samplesize.pdf", pagesize=(8.5 * inch, 11.0 * inch))
# While this already allows us to create any page format we want, reportlab comes with even more comfortable standards:

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import A5
# further possible dimensions contained in the 'pagesizes' module are:
# A0 to A10
# LETTER
# LEGAL
# TABLOID

my_a4_canvas = Canvas("a4_defaultsize.pdf", pagesize=A4)  # simply provide a single argument instead of a tuple here
my_a5_canvas = Canvas("a5_defaultsize.pdf", pagesize=A5)  # simply provide a single argument instead of a tuple here


# The following are opportunities on RESETTING THE FONT AND FONT SIZE before using the '.drawString()' method.
# The solution for tasks like these is the Canvas class's '.setFont()' method:

my_font_canvas = Canvas("font-example.pdf", pagesize=A4)
my_font_canvas.setFont("Times-Roman", 14)  # here we choose to set the standard font and size to Times New Roman 14 pt.

# There are 3 font defaults available from the beginning on:
# "Courier"
# "Helvetica"
# "Times-Roman"

# Apart from that, there are three default formats for each of the fonts mentioned above:
# "Courier"
# "Courier-Bold"
# "Courier-BoldOblique"
# "Courier-Oblique"

# "Helvetica"
# "Helvetica-Bold"
# "Helvetica-BoldOblique"
# "Helvetica-Oblique"

# "Times-Roman"
# "Times-Bold"
# "Times-BoldItalic"
# "Times-Italic"

# Now let's write a short string to our canvas:
my_font_canvas.drawString(5 * cm, 10 * cm, "This text was written in: Times New Roman, 14 pt.")
my_font_canvas.save()


# The following are opportunities on RESETTING THE FONT COLOR before using the '.drawString()' method.
# The solution for tasks like these is the Canvas class's '.setFillColor()' method:
my_font_color_canvas = Canvas("font-color-example.pdf", pagesize=A4)
my_font_color_canvas.setFont("Times-Roman", 14)
from reportlab.lib.colors import blue  # we could also import quite whatever color we wanted at this line
my_font_color_canvas.setFillColor(blue)

# Now let's write a short string to our canvas:
my_font_color_canvas.drawString(5 * cm, 10 * cm, "This text was written using the font color <blue>")
my_font_color_canvas.save()


# These examples only scratched the surface. For more information, refer to the ReportLab User Guide under:
url_1 = "https://realpython.com/pybasics-reportlab-source"
url_2 = "www.reportlab.com/docs/reportlab-userguide.pdf"
