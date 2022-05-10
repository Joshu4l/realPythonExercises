# INTRODUCTION TO ENCRYPTION OF PDF FILES AND WORKING WITH ENCRYPTED ONES

# Python offers a built-in method for encrypting PDFs. It is called '.encrypt()'
# Let's see how to use it:

# The file to practice this shall be 'newsletter.pdf' within in your 'practice_files' directory

# Do the necessary imports
import pathlib
import PyPDF2

# Set up respective path objects for our practice directory, for the file we want to work with  as well as for the resulting file
practice_dir = pathlib.Path.cwd() / "practice_files"
filepath = practice_dir / "newsletter.pdf"
resultpath = practice_dir / "newsletter_encrypted.pdf"
resultpath.touch(exist_ok=True)


# Set up a <FileReader> object for our file
fr = PyPDF2.PdfFileReader(str(filepath))
# Set up a <FileWriter> object for our resulting (encrypted) file
fw = PyPDF2.PdfFileWriter()
fw.appendPagesFromReader(fr)  # Use '.appendPagesFromReader' to populate it with just every page that our <FileReader> found

# Now let's do our first file encryption!
# TWO THINGS TO KNOW HERE, IN ORDER TO DO SO:

# 1.    Pythons '.encrypt()' method takes in two possible arguments:
# 		user_pwd	--> if set, it only allows for opening and reading the PDF
#		owner_pwd	--> if set, it allows for opening PDFs without restrictions, including editing

# 2. 	ENcryption of PDFs is always done via the File WRITER(!), NOT the FileReader!
#		makes sense because we are making changes to the document which requires an editing(wb) mode
# 		reading on the other hand is then used for DEcrypting the PDF again


# So let's define a user password as well as an owner password
user_pwd = "SuperSecret"
owner_pwd = "ReallySuperSecret"
# Now encrypt our file with both of them, so that depending on which pw is typed in, the user will have different permissions
fw.encrypt(user_pwd=user_pwd, owner_pwd= owner_pwd)

# Finally, open the result file and paste the contents, which our <FileWriter> currently holds
with resultpath.open(mode="wb") as result:
	fw.write(result)
