# REMARK: in this example it's necessary to have TWO 'while True' blocks
# The reason is that we want to give the user the ability to make revisions DIRECTLY AFTER sth went wrong.


while True:  # As long as it works properly do everything in the 'try'-block
    try:
        num1 = int(input("your first number here: "))
        break

    except ValueError:
        print("Nope. That was not an integer! Try again.")


while True:  # This part needs his own 'while True' clause too
    try:
        num2 = int(input("your second number here: "))
        content = num1 / num2
        print(f"the content of dividing {num1} by {num2} is = {content}")
        break

    except ValueError:
        print("Nope. That was not an integer! Try again.")

    except ZeroDivisionError:
        print("Division by zero is not possible! Try again and revise your num2.")
