"""Create a currency calculator with fixed type of currency"""

print("Let's see the total in US dollars of currency you have!\n")
euro_coin = float(input('How much euros you have with you? '))
yen_coin = float(input('How much yens you have with you? '))
peso_coin = float(input('How much pesos you have with you? '))
pound_coin = float(input('How much British pounds you have with you? '))

"""This convesions are dated from 2025"""
euro_val = euro_coin * 1.08
yen_val = yen_coin * 0.0067
peso_val = peso_coin * 0.059
pound_val = pound_coin * 1.27

total = euro_val + yen_val + peso_val + pound_val

print(f'The total you have in US dollars is {total:.2f}\n')
