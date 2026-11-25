"""Create a Roller Coaster height and money detector"""

height = float(input('Enter your height in cm: '))
money = float(input('Enter your current balance: '))

if height >= 137 and money >= 10:
    print('Enjoy the ride!\n')
elif height < 137 and money >= 10:
    print('You are not tall enough for this ride.\n')
elif height >= 137 and money < 10:
    print("You don't have enough money for this ride.\n")
else:
    print('You are not tall enough nor do you have enough money.\n')
