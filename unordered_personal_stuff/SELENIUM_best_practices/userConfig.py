from configparser import ConfigParser

def config(filename="userdata.ini", section="userdata"):

	parser = ConfigParser()
	parser.read(filename)
	login_config = {}

	if parser.has_section(section):
		params = parser.items(section)

		for param in params:
			login_config[param[0]] = param[1]
	else:
		raise Exception(f"no such section '{section}' found in '{filename}'!")

	return login_config