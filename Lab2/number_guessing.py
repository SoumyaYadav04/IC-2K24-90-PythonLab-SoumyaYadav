import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100")
print("You have 7 attempts")

while attempts < 7:

    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < number:
        print("Too low")

    elif guess > number:
        print("Too high")

    else:
        print("Correct!")
        print("Attempts taken:", attempts)
        break

else:
    print("You ran out of attempts")
    print("The correct number was:", number)