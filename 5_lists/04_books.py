"""
Create a list of your favorite books.
Print the whole list.
Learn to use append, insert, remove, and pop.
"""

books = ['The Book Thief',
         'The Hunger Games',
         'The Love Hypothesis',
         'Frozen Blood',
         'Kingdom of the Wicked',
         'The Great Gatsby']

print(books)

# append is used to add an element to the end of the list
books.append('The Fault in Our Stars')
print(books)

# insert is used to add an element to a specific index
books.insert(3, 'The Star Man')
print(books)

# remove is used to remove an element from the list
books.remove('The Great Gatsby')
print(books)

# pop is used to remove the last element from the list
books.pop()
print(books)
