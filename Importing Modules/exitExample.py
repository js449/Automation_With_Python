import sys

# This program has an infinite loop with no break statement inside. 
# The only way this program will end is if the execution reaches the sys.exit() call. 
# When response is equal to 'exit', the line containing the sys.exit() call is executed. 
# Since the response variable is set by the input() function, 
# the user must enter exit in order to stop the program.

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')