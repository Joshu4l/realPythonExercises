# INTRODUCTION TO DECRYPTING PDFs AND ENABLING EDITS TOWARDS ENCRYPTED PDFs

# Remember from module '9.17_PdfHandling_encrypt', that ENcryption is always done via PdfFileWriters
# and DEcryption is always done via PdfFileReaders !

# Python offers a built-in method for encrypting PDFs. It is called '.decrypt()'
# Let's see how to use it:

# The file to practice this shall be 'newsletter_encrypted.pdf' within in your 'practice_files' directory

# Do the necessary imports
import pathlib
import PyPDF2
# Set up respective path objects for our practice directory as well as for the file we want to work with
practice_dir = pathlib.Path.cwd() / "practice_files"
filepath = practice_dir / "newsletter_encrypted.pdf"
print(filepath.exists())

# So, let's do our first file decryption!
# TWO THINGS TO KNOW HERE, IN ORDER TO DO SO:

# 1.    Just like '.encrypt()',  Pythons '.decrypt()' method takes in two possible arguments:
# 		user_pwd	--> if set, it only allows for opening and reading the PDF
#		owner_pwd	--> if set, it allows for opening PDFs without restrictions, including editing

# 2. 	ENcryption of PDFs is always done via the File WRITER(!), NOT the FileReader!
#		makes sense because we are making changes to the document which requires an editing(wb) mode
# 		reading on the other hand is then used for DEcrypting the PDF again


# Set up a <FileReader> object for our file
fr = PyPDF2.PdfFileReader(str(filepath))

# Now, let's use the passwords we set earlier to actually DECRYPT and open our PDF through or FileReader!
user_pwd = "SuperSecret"
owner_pwd = "ReallySuperSecret"

# fr.getPage(0)
# Note: the usage of 'fr.getPage(0)' alone would throw an error here because of the encryption
fr.decrypt(password=user_pwd)

# When actually printing this statement, we get an exit code ranging from 0 to 2
print(fr.decrypt(password=user_pwd))
# explanation of what those codes want to express:
# 	'0'		indicates that the password was incorrect
# 	'1'		indicates that the user password was matched
# 	'2'		indicates that the owner password was matched

# Now that we decrypted the file we can access its information just like we used to with unencrypted files
print(fr.getPage(0))
