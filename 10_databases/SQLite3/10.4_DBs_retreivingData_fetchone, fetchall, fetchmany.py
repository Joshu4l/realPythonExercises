import sqlite3

db_table = """
	CREATE TABLE IF NOT EXISTS People(
		FirstName TEXT,
		LastName TEXT,
		Age INTEGER
		);"""


my_values = (
	('Ron', 'Obvious', 42),
	('Luigi', 'Vercotti', 43),
	('Arthur', 'Belling', 28)
)

db_insert = """
	INSERT OR REPLACE INTO People
	VALUES(?, ?, ?)
	;"""


with sqlite3.connect(':memory:') as db:
	db_cursor = db.cursor()

	db_cursor.execute(db_table)
	db_cursor.executemany(db_insert, my_values)  # REMEMBER that the values provided must be or consist of: tuples!

	result1 = db_cursor.execute("SELECT * FROM People;").fetchall()
	result2 = db_cursor.execute("SELECT * FROM People;").fetchmany(2) # does the exact same thing due to the non-reuseability of 1
	result3 = db_cursor.execute("SELECT * FROM People;").fetchone()  # does the exact same thing due to the non-reuseability of 1


	# EXAMPLE OF WHAT THE OUTPUTS OF EACH 'FETCH'-METHOD LOOK LIKE:
	print(f"result for 'fetchone()':   {result3}")
	print(f"result for 'fetchall():'   {result1}")
	print(f"result for 'fetchmany(2)': {result2}")

	print("\n")

	# EXAMPLE ON HOW TO SEARCH/RETRIEVE DATA BASED ON A CONDITION ('WHERE'):
	db_select_where = db_cursor.execute("SELECT FirstName, LastName FROM People WHERE Age <30").fetchall()
	print("the only person younger than 30 years is:")
	for i in db_select_where:
		print(i[0], i[1])  # prints FirstName and LastName

