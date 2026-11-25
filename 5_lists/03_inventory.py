"""
Create a quick inventory of numbers
Print the min, max, sum, and average
Sort the list (ascending and descending)
"""

inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# Min value of the list
print(min(inventory))

# Max value of the list
print(max(inventory))

# Sum of the list
print(sum(inventory))

# Average of the list
print(sum(inventory) / len(inventory))

# Sort the list in ascending order
print(sorted(inventory))

# Sort the list in descending order
print(sorted(inventory, reverse=True))
