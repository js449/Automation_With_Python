#Chapter 4 - Functions

# Functions are a way to organize your code into reusable blocks.
# They allow you to define a block of code that can be executed whenever you call the function by its name.
# Functions can take arguments, which are values passed to the function when it is called.


# def hello():
#     # Prints three greetings
#     print('Good morning!')
#     print('Good afternoon!')
#     print('Good evening!')

# # Calling the function
# hello()

# def say_hello_to(name):
# # Prints three greetings to the name provided
#     print('Good morning, ' + name)
#     print('Good afternoon, ' + name)
#     print('Good evening, ' + name)

# say_hello_to('Alice')
# say_hello_to('Bob')


# Consider adding a space after 'Hello' by setting end=' ' or
#  including a space in the string to improve readability of the output.
print('Hello', end='')
print('World')

# could replace the default separating string by passing the sep named parameter a different string
print('cats', 'dogs', 'mice', sep=',') 