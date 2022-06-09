import psycopg2
from config import config

def connect():

	params = config()

	try:
		with psycopg2.connect(**params) as con:
			cur = con.cursor()
			query = """SELECT version();"""
			cur.execute(query)
			print(cur.fetchone())

	except(Exception, psycopg2.DatabaseError) as error:
		print(error)

connect()
