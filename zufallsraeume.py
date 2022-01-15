# stuff
rooms = ["BEDROOM #1", "BEDROOM #2", "BEDROOM #3", "LIVINGROOM"]
fellas = ["Flo", "Nikola", "Vanessa", "Josh"]

# modules
from random import choice

claims = []
while len(claims) < 4:

	c = choice(fellas)
	if c in claims:
		continue
	else:
		claims.append(c)

assignments = [[a] for a in claims]

step = 0
for r in rooms:
	assignments[step].insert(0, r)
	step += 1

print(f'\n{"*"*12}RESULTS{"*"*12}')

for a in assignments:
	print(f"\n"
		  f"{a[0]}:   {a[1]}"
		  f"\n")

print(f'{"*"*31}\n')


