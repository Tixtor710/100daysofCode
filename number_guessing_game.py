import random

number = random.randint(0,10000)
tries= 0
found = False

while not found:
    guess = int(input("Guess the number:"))
    tries+= 1
    if guess == number:
        found = True
        print(f"You Have Found the Number{number} after {tries} Tries.")
    elif guess > number:
        print("The Number you are looking for is less than the guess")
    else:
        print("The Number you are looking for is greater than the guess")