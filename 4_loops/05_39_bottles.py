"""
Create a code that generates a loop that counts bottles of beer.
Loop should run 39 times.
"""

for i in range(39, 0, -1):
    bottles = "bottles" if i > 1 else "bottle"
    next_bottles = "bottles" if (i - 1) != 1 else "bottle"

    if i > 38:
        print(f'{i} {bottles} of beer on the wall')
        print(f'{i} {bottles} of beer')
        print('Take one down, pass it around\n')
    else:
        print(f'{i} {bottles} of beer')
        print('Take one down, pass it around\n')

    if i - 1 > 0:
        print(f'{i-1} {next_bottles} of beer on the wall')
    else:
        print('No more bottles of beer on the wall!\n')
