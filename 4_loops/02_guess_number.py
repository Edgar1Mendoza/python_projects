"""
Create a code that checks if the user can guess the number correctly.
If it's not, then do a loop to ask the user to enter the correct number.
This time it has limited attempts.
"""

import random

number = random.randint(1, 10)
attempts = 0

while attempts < 5:
    guess = int(input('Guess the number from (1-10): '))

    if guess == number:
        print('You guessed the correct number!')
        break
    elif attempts == 4:
        break
    else:
        attempts += 1
        print('Thats not it. Try again.')

if attempts == 4:
    print('You run out of attempts.\n')
else:
    print('\n')
