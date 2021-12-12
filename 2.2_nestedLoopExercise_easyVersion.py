# Ask user for two number Inputs
x = float(input("Please number:"))
y = int(input("How often should it be doubled: "))

def multiply(x,y):
    # Pull the global scope variables from outside in here
    num = x
    times = y

    # Loop over a range of (1 until users repetition input)
    for i in range(1,times+1):
        # re-use the duplication result again within itself
        num = num * 2
        # print all: first, intermediate, last results
        print(num)
    return num

# no need to type "print() here !  Because printing a result is already included in the function's body
multiply(x,y)
