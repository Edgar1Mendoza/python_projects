"""
Create a code that checks if the entered PIN code is correct. If it's not,
then do a loop to ask the user to enter the correct PIN code
"""

print('\n----- Bank of the Future -----')

pin = int(input('Enter your PIN code: '))

while pin != 1234:
    pin = int(input('Incorrect PIN code. Try again: '))

print('\nYou entered the correct PIN code!')
