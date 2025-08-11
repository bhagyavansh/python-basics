secret = 7

print("Guess the secret number!")

while True:
    Guess = int(input("Enter the guessed number: "))
    if Guess == secret:
        print("Success")
        break
    else:
        print("Try again")
