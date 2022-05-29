import sqlite3

db_table_query = """
	CREATE TABLE IF NOT EXISTS Courses(
		course_id INTEGER PRIMARY KEY,
		CourseName TEXT,
		CourseProf TEXT,
		ECTS INTEGER
	);"""


# Data to be inserted:
courses = [
	(1, 'Projektmanagement', 'Christian Bär', 5 ),
	(2, 'Digital Intrapreneurship & Innovationsmanagement', 'Gunter Herr', 5),
	(3, 'Wissenschaftliche Forschungsmethoden', 'Fritjof Karnani', 5),
	(4, 'Führung & Kommunikation', 'Fritjof Karnani', 5),
	(5, 'Statistik Advanced', 'Udo Bankhofer', 5),
	(6, 'Cybersecurity', 'Thomas Bosch', 5),
	(7, 'Cyberphysical Production Systems', 'Rainer Lasi', 5)
]  # IMPORTANT here: when providing data for a SQL query, it MUST CONSIST OF TUPLES in order to be accepted by the ?-notation!


# using the ?-notation here, so our query gets INJECTION-PROOF and easier to fill with multiple values!
# This is called PARAMETERIZED STATEMENTS
db_insert_query = """
					INSERT OR REPLACE INTO Courses
					VALUES(?, ?, ?, ?);
					"""  # Using the 'OR REPLACE' specification here (so when a value for an existing course_id changes, it will be updated)

# simply do an individual search for some courses
db_select_query = """
	SELECT course_id, CourseName, CourseProf, ECTS
	FROM Courses;
	"""




# Example for creating an IN MEMORY database
with sqlite3.connect(":memory:") as db_connection:
	# Using the ':memory:' keyword will cause the DB object to only exist and run TEMPORARILY (in our RAM)
	# Thus, perfect for testing purposes! :)

	db_cursor = db_connection.cursor()  # set up a cursor

	db_cursor.execute(db_table_query)  # execute a statement for creating a table

	# Example for inserting several values at once using the '.executemany()' method:
	db_cursor.executemany(db_insert_query, courses)
		# IMPORTANT TO KNOW HERE:
		# Our <courses> variable here is being provided as an additional parameter to our '.execute()' method
		# Whereas the value of additional parameters passed into '.execute()' or '.executemany()' ...
		# ...MUST ALWAYS BE OR CONSIST OF TUPLES!!


	# using the select query defined above, now show each resulting row
	results = db_cursor.execute(db_select_query)
	for i in results.fetchmany(10):
		print(i)

