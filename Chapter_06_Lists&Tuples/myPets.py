# This program checks if a pet name is in the list of pets.
# in and not in are membership operators that check for the presence of a value in a list.

my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


# List Comprehensions
# List comprehensions provide a concise way to create lists.
squares = [x**2 for x in range(10)]  # Creating a list of squares
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 