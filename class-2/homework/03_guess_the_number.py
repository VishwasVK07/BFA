# Homework 3: Guess the number
# ------------------------------------------------------------
# TOPICS: variables, while loop, break, if / elif / else, input, f-strings
#
# PROBLEM
# Set secret = 7 in your code. Use a while loop to keep asking the user for a
# guess (convert with int()). Count the tries in a variable. Print Too low or
# Too high after each wrong guess. When the guess is right, break and print how
# many tries it took.
#
# EXPECTED OUTPUT (your program should behave like this)
#   Guess: 3
#   Too low
#   Guess: 9
#   Too high
#   Guess: 7
#   Correct! You took 3 tries.
# ------------------------------------------------------------
# Write your code below this line

secret = 7
tries = 0

while True:
    guess = int(input("Your guess:"))
    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct, you took {tries} tries.")
        break