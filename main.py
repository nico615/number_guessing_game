import random
from art import logo
print(logo)

rand_num = random.randint(1, 100)
print(rand_num)

guesses_easy = 10
guesses_hard = 5

def set_difficulty():
    diff = input("easy or hard game?")
    if diff == "easy":
        return guesses_easy
    if diff == "hard":
        return guesses_hard

game_running = True
guesses = set_difficulty()
while game_running:

    guess = int(input("Guess a number."))
    if guess == rand_num:
        print("That's the number! You won. ")
        game_running = False
    elif guesses <= 1:
        print(f"You lost. The solution was {rand_num}")
        game_running = False
    elif guess < rand_num:
        print("Too low. Try another guess")
        guesses -= 1
        print(f"You have {guesses} guesses remaining.")
    elif guess > rand_num:
        print("Too high. Try another guess")
        guesses -= 1
        print(f"You have {guesses} guesses remaining.")
