import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = 7

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number within the range {lower_bound}-{upper_bound}.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
