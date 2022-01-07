import pathlib

rpe = pathlib.Path().cwd()
for element in list(rpe.glob("*6.*")):
	element = element.name[0].replace("6", "5") + element.name[1:]
	new = rpe / element
	new.touch()
	#element.touch()


