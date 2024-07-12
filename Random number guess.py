import random 

secret_number = random.randint(1, 20)

print("Welcome to the Guessing Game !!")
print("Try to guess the secret number between 1 and 20.")

# Set initial values
attempts = 0
max_attempts = 5
guess = None

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the secret number in", attempts + 1, "attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    attempts += 1

# If the player couldn't guess within the allowed attempts
if guess != secret_number:
    print("Sorry, you've run out of attempts. The secret number was:", secret_number)
