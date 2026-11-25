"""Create a coin flip game where the result is always pseudo-random"""

import random

coin = random.randint(0, 1)

if coin < 0.5:
    print('Heads')
else:
    print('Tails')
