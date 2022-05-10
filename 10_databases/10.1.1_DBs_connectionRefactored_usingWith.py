# In comparison to module '10.0_DBs_introduction.py', we will use a 'with'-statement this time
# This will result two main advantages: cleaner code, connection will automatically be closed after the indented block

# 1st: import the 'sqlite3' package
import sqlite3

# 2nd: Connect to an existing database or create a new one
with sqlite3.connect("test_database.db") as db_connection:
	db_cursor = db_connection.cursor()
# 3rd: Execute SQL statements on the database (which requires a cursor object)
	db_query = "SELECT datetime('now', 'localtime');"
	query_result = db_cursor.execute(db_query)
	result_row1 = query_result.fetchone()
	result_row1_col1 = result_row1[0]
	print(result_row1)
	print(result_row1_col1)
# 4th: Close the database connection (happens automatically here thanks to the with statement)