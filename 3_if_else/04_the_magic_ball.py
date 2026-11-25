"""Create a magic ball that gives you answers out randomly"""

import random

question = input('Ask any question: ')

random_number = random.randint(1, 9)

if random_number == 1:
    answer = 'Yes, definitely'
elif random_number == 2:
    answer = 'If you desire it strongly enough, yes'
elif random_number == 3:
    answer = 'Cannot predict now'
elif random_number == 4:
    answer = 'Concentrate and ask again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'It is decidedly so'
else:
    answer = 'Error'

print('Magic 8 Ball says: ' + answer + '\n')
