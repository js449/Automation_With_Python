#Chapter 1 - Python basics
# 
#  This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)

print('The length of your name is:')
print(len(my_name))
print(type(my_name))  # This will show that my_name is a string.

print('What is your age?')  # Ask for their age.
my_age = input('>')
intAge = int(my_age)
print(type(intAge))  # This will show that my_age is a int.
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
print(type(my_age)) # This will show that my_age is a string

print('round() function')
# The round() function rounds a number to the nearest integer.
print(round(3.14))
print(round(7.7))
print(round(-2.2))

print('abs() function')
# The abs() function returns the absolute value of a number.
print(abs(25))
print(abs(-25))
print(abs(-3.14))
print(abs(-3.14))


#Notes
# The input() function always returns a string, even if the user enters a number.

# The my_age variable contains the value returned from input() 
# Because the input() function always returns a string (even if the user entered a number),
#  you can use the int(my_age) code to return an integer value of the string in my_age.
#  This integer value is then added to 1 in the expression int(my_age) + 1.

                       # TEXT AND NUMBER EQUIVALENCE

# Although the string value of a number is considered a completely different value from the integer or floating-point version,
# an integer can be equal to a floating point:

                        # >>> 42 == '42'
                        # False
                        # >>> 42 == 42.0
                        # True
                        # >>> 42.0 == 0042.000
                        # True
# Python makes this distinction because strings are text, while integers and floats are numbers.