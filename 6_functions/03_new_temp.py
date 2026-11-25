"""
Create a temp file that can receive a user input.
The temp can be used to transform from F to C or C to F
"""

unit = input("Enter the unit you want to work with (F or C): ")
temp = float(input("Enter the temperature: "))

unit = unit.upper()

if unit == "F":
    temp = (temp - 32) * 5/9
    print(f"{temp:.2f} C")
elif unit == "C":
    temp = (temp * 9/5) + 32
    print(f"{temp:.2f} F")
else:
    print("Invalid unit.")
