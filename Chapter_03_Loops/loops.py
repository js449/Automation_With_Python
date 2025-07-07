#Chapter 3 - Loops

#Python’s two kinds of loops, while and for, 
# open up the full power of automation, because they can run lines of code millions of times per second.

# The while loop keeps looping while its condition is True (which is the reason for its name).

# spam = 0
# while spam <= 5:
#     print('Hello, world.')
#     spam = spam + 1


#Boolean values are either True or False.
name = ''
while not name:
    print('Enter your name:')
    name = input('>')
print('How many guests will you have?')
num_of_guests = int(input('>')) 
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')