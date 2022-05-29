# REMEMBER:
# Our main file will not be able to read from the .ini file directly
# BUT it can do so from this config.py file here (as it simply is another python module)

relevant_url = r"https://www.youtube.com/watch?v=Q8iYj2ypWss"

# Do the necessary lib imports
from configparser import ConfigParser
def config(filename='database.ini', section="postgresql"):  # note that the filename does NOT need to be a pathlib object here

	"""Creates a <ConfigParser> object, which reads in a specified .ini file,
	prepares a db dictionary and adds all the variables from within the .ini file
	to the dictionary in form of key-value-pairs.
	"""

	parser = ConfigParser()  # create a ConfigParser object by making use of the imported <ConfigParser> class (no params needed)
	parser.read(filename)  # use the parser's '.read()' method to read the .ini's filename (we defined as our default param above)
	db = {}  # set up an empty dictionary (to be populated by the loop below)

	if parser.has_section(section):  # verify if there even exists a section/header in our .ini file
		params = parser.items(section)  # by using the '.items()' method, we'll return a list consisting of (name, value)-tuples for each variable in our section.

		for param in params:  # iterate over each tuple contained in our 'params' list
			db[param[0]] = param[1]  # populate the db dictionary by respectively adding a key (tuple-index 0) and a value (tuple-index 1)

	else:  # if there are actually no sections in our .ini file at all:
		raise Exception(f"Section {section} was not found in the {filename} file.")	 # throw an exception

	# finally, return the config dict 'db' we populated
	return db


