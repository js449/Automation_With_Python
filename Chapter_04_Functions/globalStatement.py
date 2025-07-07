# This code demonstrates the use of the global statement in Python.
# The global statement allows you to modify a variable defined outside the current scope.
# When you declare a variable as global, you can change its value within a function,
# affecting its value in the global scope.
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)  # Prints 'spam'