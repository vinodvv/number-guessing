import random

number_to_guess = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess that number.")

for i in range(max_attempts):
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulation! "
                  f"You've guessed the correct number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter your guess.")


else:
    print(f"Sorry, you have used all {max_attempts} attempts. "
          f"The correct number was {number_to_guess}.")
