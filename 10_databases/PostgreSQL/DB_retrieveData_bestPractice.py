import psycopg2
from config import config

def retrieve_data():

	params = config()  # this line assigns the config() -function's output to a variable we're gonna use below

	try:
		with psycopg2.connect(**params) as con:

			cur = con.cursor()

			query = """SELECT * FROM person;"""  # similar line to the one used in the 'connect' best practice file
			cur.execute(query)

			return cur.fetchall()

	except(Exception, psycopg2.DatabaseError) as error:
		print(error)


# call the function and iterate over the result
for row in retrieve_data():
	print(row)
