"""Create the famous Harry Potter sorting hat \
    that will decide which house they belong to \
    based on their answers"""

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('\n|------------- Welcome to The Sorting Hat -------------|')

# Question 1 - The Break of Dawn:
print('\nWhat kind of landscape inspires you most upon waking?')
print(' 1- The roar of the ocean crashing against jagged cliffs')
print(' 2- A sun-drenched garden teeming with flowers and honeybees')
print(' 3- An ancient library bathed in the soft glow of morning light')
print(' 4- A sleek, high-rise office overlooking a city ripe for the taking')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    slytherin += 1
else:
    print('Wrong input!')

# Question 2 - The Encounter:
print('\nA wide, raging river blocks your path. How do you cross?')
print(' 1- Dive right in and swim across; the danger is part of the thrill')
print(' 2- Gather fellow travelers and work together to build a sturdy bridge')
print(' 3- Study the currents and engineer a clever way to cross the river')
print(' 4- Negotiate with someone to ferry you across in exchange for a favor')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    slytherin += 1
else:
    print('Wrong input!')

# Question 3 - The Enchanted Chest:
print('\nYou stumble upon a mysterious chest. What do you hope to find inside')
print(' 1- An ancient sword that once belonged to a legendary hero')
print(' 2- A magical seed that grows into a never-ending harvest \
      to share with all')
print(" 3- A forgotten scroll w/ the answers to all the universe's mysteries")
print(' 4- A ring that grants you the power to influence the minds of others')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    slytherin += 1
else:
    print('Wrong input!')

# Question 4 - The Legacy:
print('\nHow would you like to be remembered by history?')
print(' 1- As "The Brave", who never wavered in the face of fear')
print(' 2- As "The Loyal Friend", whom everyone could count on')
print(' 3- As "The Wise", who enlightened the world with their intellect')
print(' 4- As "The Great Leader", who scaled the heights of power and success')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
    gryffindor += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    slytherin += 1
else:
    print('Wrong input!')

higher_count = max(gryffindor, hufflepuff, ravenclaw, slytherin)

if gryffindor == higher_count:
    print('\nYou are a Gryffindor!\n')
elif hufflepuff == higher_count:
    print('\nYou are a Hufflepuff!\n')
elif ravenclaw == higher_count:
    print('\nYou are a Ravenclaw!\n')
else:
    print('\nYou are a Slytherin!\n')
