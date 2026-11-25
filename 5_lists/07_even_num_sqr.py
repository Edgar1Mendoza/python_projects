"""
Create a new list in a sigle line of code and print it.
The list should contain all the even numbers squared.
Moreover, print the length of the list.
Combine two lists at the end.
"""

# Squares for even numbers
squares = [x**2 for x in range(10) if x % 2 == 0]

print(squares)  # Output: [0, 4, 16, 36, 64]

# Print the length
print(len(squares))  # Output: 5

# Combine two lists
squares_2 = [100, 144, 196, 256]
tenth_value = pow(18, 2)  # Use the pow() function to calculate 18^2
squares_2.append(tenth_value)  # Add the 18^2 value to the list
combined_list = squares + squares_2

print(combined_list)
# Output: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
