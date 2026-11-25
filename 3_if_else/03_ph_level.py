"""Create a ph level reader that can tell if \
    a sustance is Alkaline, Acidic or Neutral"""

ph = float(input('\nEnter the ph level range(0-14): '))

if ph > 0 and ph < 7:
    print(f'Ph level {ph:.2f} is Acidic\n')
elif 7 < ph <= 14:
    print(f'Ph level {ph:.2f} is Alkaline\n')
elif ph == 7:
    print(f'Ph level {ph:.2f} is Neutral\n')
else:
    print(f'Ph level {ph:.2f} is out of the range\n')
