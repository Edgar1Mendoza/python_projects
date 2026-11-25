"""Create a better version of the Roller Coaster \
    height and money detector"""

ride_is_open = True
height = float(input('Enter you height in cm: '))
money = float(input('Enter your current balance: '))

tall_enough = height >= 137
enough_money = money >= 10

if ride_is_open and tall_enough and enough_money:
    print('Enjoy the ride!\n')
elif enough_money and not tall_enough:
    print('You are not tall enough for this ride.\n')
elif tall_enough and not enough_money:
    print("You don't have enough money for this ride.\n")
elif not tall_enough and not enough_money:
    print('You are not tall enough nor do you have enough money.\n')
else:
    print('Sorry, this ride is closed.')
