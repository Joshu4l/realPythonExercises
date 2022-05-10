# INTRODUCTION ON
# - HOW TO CONNECT TO AN EXISTING DATABASE
#   OR (in absence of an existing one)
# - HOW TO CREATE A NEW DATABASE CONNECTION

# Basis for those activities is pythons standard lightweight DBMS package 'sqlite3'
# Let's see what we can use it for:

# INTERACTIONS WITH A SQLITE3-DATABASE TYPICALLY FOLLOW 4 STEPS:

# 1st: Import the sqlite3 package
import sqlite3


# 2nd: Connect to an existing database or create a new one
db_connection = sqlite3.connect("test_database.db")
	# if this is the name of an existing db, python will connect to it, otherwise a new one is created
	# note that Databases are referred to with the suffix '.db' (just like a file extension)


# 3rd: Execute SQL statements on the database (which requires a cursor object)
db_cursor = db_connection.cursor()
	# in database jargon, a cursor is an object which fetches query results one row at a time
db_query = "SELECT datetime('now', 'localtime');" # don't forget the semicolon at SQL statements!
query_result = db_cursor.execute(db_query)
	# the setup/structure is always the same:
		# cursor
			# .execute()
				# query
result_row1 = query_result.fetchone()
print(result_row1)  # actually let the program return the first row of our query result
# this returns a TUPLE
# depending on how much we want to get back we would have the following opportunities:
	# fetchone () /
	# fetchmany(int) /
	# fetchall ()
print(result_row1[0])  # actually let the program return the first value of the first row of our query result


# 4th: Close the database connection
db_connection.close()
