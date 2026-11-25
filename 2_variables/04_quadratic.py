"""Create a quadratic calculator, ask the user for the imputs"""

a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))

root_1 = ((-b + (b*b - 4*a*c)**0.5) / 2*a)
root_2 = ((-b - (b*b - 4*a*c)**0.5) / 2*a)

print(f'The first root is {root_1}')
print(f'The second root is {root_2}\n')
