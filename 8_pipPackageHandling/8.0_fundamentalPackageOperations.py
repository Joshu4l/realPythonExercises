# In order to verify that pip even is installed, or to verify PIP's CURRENT VERSION type the following cmd command:
	# python -m pip --version


# In order to UPGRADE PIP to the latest version, type the following cmd command:
	# python -m pip install --upgrade pip


# In order to see which packages are CURRENTLY INSTALLED/AVAILABLE, type the following cmd command:
	# python -m pip list


# In order to actually INSTALL a third party package, type the following cmd command:
	# python -m pip install <name_of_the_package>


# In order to install a specific version of a third party package, type the following cmd command:
	# python -m pip install 'name_of_the_package'
	# 		at the end of this line we can choose between several version specifiers:
	# 											1. inclusive less than, or inclusive greater than:  <= , >=
	# 											2. exclusive less than, or exclusive greater than:  < , >
	# 											3. exactly equal to:  ==
	# example statement:
	# python -m pip install requests>=2.0
	# example statement with a version specifier combination:
	# python -m pip install requests>=1.5,<=2.0


# In order to SHOW PACKAGE DETAILS, of an installed package, type the following cmd command:
	# python -m pip show 'name_of_the_package'
	#
	# example statement:
	# python -m pip show requests


# In order to UNINSTALL A PACKAGE, type the following cmd command:
	# python -m pip uninstall 'name_of_the_package'
	#
	# example statement:
	# python - pip uninstall requests
	#
	# requires user approval by pressing (y / n)
	#
	# example statement for uninstalling several packages at once
	# python -m pip uninstall request certifi chardet idna urllib3

