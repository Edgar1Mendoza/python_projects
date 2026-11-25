"""Create an if-else grade system where it determines \
    if you fail or pass based on your grade"""

grade = float(input('Enter your grade: '))

if grade > 70:
    print(f'You passed!\n{grade:.1f} is a passing grade\n')
else:
    print(f'You failed!\n{grade:.1f} is a failing grade\n')
