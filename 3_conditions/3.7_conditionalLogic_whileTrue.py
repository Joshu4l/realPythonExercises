solution = "xxx"

while True:
    guess = input("your guess: ")

    if guess.lower() == solution.lower():
        print("correct!")
        break

    else:
        print("try that again.")
