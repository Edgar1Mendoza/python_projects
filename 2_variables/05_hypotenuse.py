"""Create a hypotenuse calculator, ask the user for two int and calculate it"""

a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

c = (a**2 + b**2) ** 0.5

print(f'The hypotenuse of the values a = {a} and b = {b} is {c:.1f}\n')
