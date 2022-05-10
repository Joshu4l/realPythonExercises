# Basis for this little exercise was:
url = r"https://www.youtube.com/watch?v=sugvnHA7ElY&ab_channel=CoreySchafer"

# Note to myself: The purpose of this module is demonstration of what the expression
# 	if __name__ == '__main__':
# actually means.

# This module only works / gets understandable in combination with module 'second_module'
# So go ahead and check what's the content of that one, and execute it.
# In comparison to that, click on RUN for 'first_module' directly


print("This sentence is printed always")

def main():
	print(f"This code was run because the module itself was RUN DIRECTLY")

if __name__ == '__main__':
	main()
else:
	print(f"Note: this line is shown because we are not running the module '{__name__}' directly BUT BY IMPORTING IT!")
