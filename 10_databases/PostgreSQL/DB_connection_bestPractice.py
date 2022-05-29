# Do the necessary library import
import psycopg2
from config import config

# Establish a connection object
	# BUT THIS TIME, USING THE CONTENTS OF A CONFIGURATION (or "INI-") FILE:

	# An INI file is a configuration file for software, that consists of a text based content,
	# with a structure and syntax containing key-value pairs for properties,
	# and sections that organize the properties.

def connect():

	"""Establishes a database connection by making use of the database parameters,
	which are returned by our config module's  'config' method"""

	params = config()  # IMPORTANT: THIS IS WHERE WE ACTUALLY MAKE USE OF THE PARAMS DEFINED IN OUR config.py

	try:
		with psycopg2.connect(**params) as con:

			print("Trying to connect to PostgreSQL database ...")  # Indicate on the console that we're about to connect to our DB
			cur = con.cursor()  # set up a cursor

			print("Connected to PostgreSQL database, version: ")
			cur.execute("SELECT version();")  # query the DB version currently in use
			db_version = cur.fetchall()  # assign the query result to a variable
			print(db_version)

	# In case sth goes wrong, provide psycopg2's Database Error message:
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

if __name__ == '__main__':  # turn the module into a SCRIPT by saying "as soon as the .py-file is opened it also will be run instantly"
	# Finally, call our function
	connect()
