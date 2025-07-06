# There are only two differences between the tuple data type and the list data type. 
# The first difference is that you write tuples using parentheses instead of square brackets. 
# For example, enter the following into the interactive shell:

spam = ('cat', 'bat', 'rat', 'elephant')
 
#  The second and primary way that tuples are different from lists is that tuples, 
# like strings, are immutable: you can’t modify, append, or remove their values. 
# Enter the following into the interactive shell, and look at the resulting TypeError error message:

# spam[1] = 'aardvark'  # TypeError: 'tuple' object does not support item assignment    
# spam.append('dog')  # AttributeError: 'tuple' object has no attribute 'append'
# spam.remove('bat')  # AttributeError: 'tuple' object has no attribute 'remove'
# spam.pop()  # AttributeError: 'tuple' object has no attribute 'pop'
# spam.insert(1, 'dog')  # AttributeError: 'tuple' object has no attribute 'insert'
# spam.extend(['dog', 'fish'])  # AttributeError: 'tuple' object has no attribute 'extend'
# spam.sort()  # AttributeError: 'tuple' object has no attribute 'sort'
# spam.reverse()  # AttributeError: 'tuple' object has no attribute 'reverse'
# spam.clear()  # AttributeError: 'tuple' object has no attribute 'clear'
# spam.count('cat')  # AttributeError: 'tuple' object has no attribute 'count'
# spam.index('bat')  # AttributeError: 'tuple' object has no attribute 'index'


# List and Tuple Type Conversion 

# You can convert a list to a tuple by passing the list to the tuple() function,
# and you can convert a tuple to a list by passing the tuple to the list() function:

spam_list = ['cat', 'bat', 'rat', 'elephant']
spam_tuple = tuple(spam_list)  # Converting list to tuple     
print(spam_tuple)  # Output: ('cat', 'bat', 'rat', 'elephant')    

spam_tuple = ('cat', 'bat', 'rat', 'elephant')
spam_list = list(spam_tuple)  # Converting tuple to list  
print(spam_list)  # Output: ['cat', 'bat', 'rat', 'elephant']


# Tuple Packing and Unpacking

# Tuples can be packed and unpacked, similar to how lists can be packed and unpacked.
# Packing a tuple means creating a tuple with multiple values, while unpacking means extracting those values    
# into separate variables. Here’s an example of packing and unpacking a tuple:

packed_tuple = ('cat', 'bat', 'rat', 'elephant')  # Packing a tuple with multiple values
a, b, c, d = packed_tuple  # Unpacking the tuple into separate variables
print(a)  # Output: cat           
print(b)  # Output: bat
print(c)  # Output: rat   
print(d)  # Output: elephant

# 