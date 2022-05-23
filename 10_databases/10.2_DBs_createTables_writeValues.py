# INTRODUCTION TO CREATING SQLite3 TABLES AND WRITING VALUES TO THEM

# IMPORTANT TO KNOW UPFRONT:
# Python strings containing SQL statements must have double quotes ("") as outer delimiters,
# whereas the inner SQL expressions themselves are ONLY valid if delimited by single quotes ('').

import sqlite3
with sqlite3.connect("test_database.db") as db_connection:

	# Using our existing <Connection> object, create a <Cursor> object now:
	db_cursor = db_connection.cursor()

	# to be uncommented when we want to reset the DB-table
	# db_cursor.execute("Drop Table People")

	# Example for creating a first DB table <People> with a total of 4 columns (id, FirstName, LastName and Age)
	sql_create_table = """
		CREATE TABLE IF NOT EXISTS People(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			FirstName TEXT,
			LastName TEXT,
			Age INT
		);"""
	# IMPORTANT THINGS TO NOTICE HERE:
		# The 'IF NOT EXISTS' expression here makes sure, to only actually create the table if it does NOT exist YET!
			# Without this expression python would run into an error.
		# The 'INTEGER PRIMARY KEY' specification can (optionally) be used to redefine / rename the primary key's ALIAS
			# If we do not actively redefine it, it will remain under its default alias <rowid>
		# The 'AUTOINCREMENT' specification makes sure that we do not have to provide a primary key manually each time.
			# It will be set in the background parallely with every INSERT INTO statement
	db_cursor.execute(sql_create_table)


	# id, FirstName, LastName, Age
	my_inputs = (1, 'Josh','Albert',27)


	# Example for inserting a handful of first datasets into the <People> table we created above:
	sql_insert = "INSERT OR REPLACE INTO People VALUES(?, ?, ?, ?);"
		# IMPORTANT THINGS TO KNOW HERE (1/2):  Notice the ?-SYNTAX
		# This makes an insert statement INJECTION-PROOF! -> this is also called PARAMETERIZED STATEMENTS
		# Thus, better practice than to simply provide the values on the spot!

		# IMPORTANT THINGS TO KNOW HERE (2/2):  Notice the 'OR IGNORE' specification
		# It is one of several SQL-extended functionalities for error handling on INSERT statements:

			# If someone attempts to insert a row with an ALREADY EXISTING id,
			# an actual INSERT execution is prevented by 'OR IGNORE'. Additionally, the (normally) resulting error will be
			# turned into a warning instead (in order to allow the program to keep running)

			# INSTEAD of simply ignoring inserts for ALREADY EXISTING IDs,
			# we could also use an 'OR REPLACE INTO' statement:
			# If an entry/row for the specified id does not exist yet, a new one will be created/inserted.
			# If an entry/row for the specified id DOES already exist, outdated values (except for the id itself) will be REPLACED!

	db_cursor.execute(sql_insert, my_inputs)
		# IMPORTANT THINGS TO KNOW HERE: Notice the usage of our <my_inputs> variable
		# The actual values to be inserted are specified as an additional parameter to the '.execute()'-method


	# Uncomment if needed:
	# db_cursor.execute("DELETE FROM People WHERE FirstName = 'Josh'")

	# Example for iterating over the resulting rows of a first SELECT-query
	for row in db_cursor.execute("SELECT id, rowid, LastName FROM People;"):
		print(row)
