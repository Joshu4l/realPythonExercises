#first user input
sth = int(input("Please put in a base integer here: "))
#second user input
exp = int(input("now your requested exponent: "))

riseToPower = sth**exp
lengthcontent = len(str(riseToPower))


multiplicationcontent = riseToPower*3

def evenOrUneven (howAmI):
    """does a modulo division to see whether even or uneven number"""
    if howAmI % 2 == 0:
        return "even"

    else:
        return "uneven"
evennesscontent = evenOrUneven(multiplicationcontent)



def integerOrFloat (x):
    """evaluates whether Integer or Float value"""
    if type(x) == int:
        return "Integer"

    elif type(x) == float:
        return "Float"

    else:
        return type()
typecontent = integerOrFloat(multiplicationcontent)


print(f"""
You put in {sth} as your base and {exp} as your exponent, that contents in {riseToPower}.
We now multiply that by e.g. 3 and get the {evennesscontent}, {lengthcontent}-digit {typecontent} of {multiplicationcontent}.
To display that a bit more structured: {multiplicationcontent: ,.2f}
""")

