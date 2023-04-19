"""Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, game"""

import random


def ask():
    while True:
        guess = input(': ')  # Enter the guess.
        
        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer.
        print('Please enter a number between 1 and 100.')
        
        
print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
secret_num = random.randint(1, 100)  # Select a random number.
print('I am thinking of a number betwwen 1 and 100.')

for i in range(10):  # Give the player 10 guesses.
    print(f'You have {10 - i} guesses left. Take a guess.')
    
    guess = ask()
    if guess == secret_num:
        break
    
    # Offer a hint
    if guess < secret_num:
        print('Your guess is too low.')
    if guess > secret_num:
        print('Your guess is too high.')
        
# Reveal the results:
if guess == secret_num:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secret_num)