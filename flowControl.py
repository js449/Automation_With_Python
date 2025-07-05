# #Chapter 2 - If Else & Flow Control
# #  This program demonstrates the use of if, elif, and else statements.  

# #Boolean values are also demonstrated.
# spam = True
# print(spam)

# # Comparison operators, also called relational operators, compare two values and evaluate down to a single Boolean value.

# print(42 == 42)  # True
# print(42!= 42 ) # False
# print(42 < 100)  # True
# print(42 > 100)  # False
# print(42 <= 42)  # True
# print(42 >= 42)  # True

# # Mixing Boolean and Comparison Operators
# print(42 == 42 and 100 > 42)  # True
# print(42 == 42 or 100 < 42)  # True
# print(not (42 == 42))  # False

# spam = 4
# print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)

# If, Elif, and Else Statements
username = 'Mary'
password = 'swordfish'
if username == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
      print('Access granted.')
    else:
      print('Wrong password.')

# If, Elif, and Else Statements with Multiple Conditions
name = 'Carol'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
else:
    print('You are neither Alice nor a little kid.')