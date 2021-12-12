#first user input
sth = int(input("Please put in a base integer here: "))
#second user input
exp = int(input("now your requested exponent: "))

riseToPower = sth**exp
lengthResult = len(str(riseToPower))


multiplicationResult = riseToPower*3

def evenOrUneven (howAmI):
    """does a modulo division to see whether even or uneven number"""
    if howAmI % 2 == 0:
        return "even"

    else:
        return "uneven"
evennessResult = evenOrUneven(multiplicationResult)



def integerOrFloat (x):
    """evaluates whether Integer or Float value"""
    if type(x) == int:
        return "Integer"

    elif type(x) == float:
        return "Float"

    else:
        return type()
typeResult = integerOrFloat(multiplicationResult)


print(f"""
You put in {sth} as your base and {exp} as your exponent, that results in {riseToPower}.
We now multiply that by e.g. 3 and get the {evennessResult}, {lengthResult}-digit {typeResult} of {multiplicationResult}.
To display that a bit more structured: {multiplicationResult: ,.2f}
""")

