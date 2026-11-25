"""Create the famous Harry Potter sorting hat \
    that will decide which house they belong to \
    based on their answers"""

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Question 1:
print('\nWhat do you prefer? 1 or 2?')
print(' 1- Day')
print(' 2- Night')

answer = int(input('Enter your answer (1-2): '))

if answer == 1:
    gryffindor = gryffindor + 1
    hufflepuff = hufflepuff + 1
elif answer == 2:
    ravenclaw = ravenclaw + 1
    slytherin = slytherin + 1
else:
    print('Wrong input!')

# Question 2:
print('\nWhen I die, I want people to remember as: ')
print(' 1- Bold')
print(' 2- Good')
print(' 3- Wise')
print(' 4- The Greatest')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor = gryffindor + 3
elif answer == 2:
    hufflepuff = hufflepuff + 3
elif answer == 3:
    ravenclaw = ravenclaw + 3
elif answer == 4:
    slytherin = slytherin + 3
else:
    print('Wrong input!')

# Question 3:
print('\nWhich instrument do you like the most: ')
print(' 1- Drums')
print(' 2- Trumpet')
print(' 3- Piano')
print(' 4- Violin')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor = gryffindor + 1
elif answer == 2:
    hufflepuff = hufflepuff + 1
elif answer == 3:
    ravenclaw = ravenclaw + 1
elif answer == 4:
    slytherin = slytherin + 1
else:
    print('Wrong input!')

if gryffindor >= hufflepuff and gryffindor >= ravenclaw and \
        gryffindor >= slytherin:
    print('\nYou are a Gryffindor!\n')
elif hufflepuff >= ravenclaw and hufflepuff >= slytherin:
    print('\nYou are a Hufflepuff!\n')
elif ravenclaw >= slytherin:
    print('\nYou are a Ravenclaw!\n')
else:
    print('\nYou are a Slytherin!\n')
