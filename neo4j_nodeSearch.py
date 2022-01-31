from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Tiger3nte"))

def get_professors(tx, name):

	# define an empty result list
	professors = []

	# set up a query using cypher language
	result = tx.run("MATCH (p:Professor)-[:teaches]->(s)"
					"RETURN p.last_name AS professor", name=name)

	# iterate over all resulting nodes and add them to the result-list
	for record in result:
		professors.append(record["professor"])

	# show the results
	return professors


with driver.session() as session:

	professors = session.read_transaction(get_professors, "Karnani")

	for prof in professors:
		print(prof)

driver.close()
