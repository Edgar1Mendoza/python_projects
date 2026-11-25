"""Create a temperature converter"""

fahrenheit = 73
celsius = 31

temp_c = (fahrenheit - 32) / 1.8
temp_f = (celsius * 1.8) + 32

print(f'First temperature is {temp_c:.1f}c')
print(f'Second temperature is {temp_f:.1f}f\n')
