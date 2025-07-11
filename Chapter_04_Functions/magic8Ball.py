# When creating a function using the def statement, 
# you can specify the return value with a return statement, which consists of the following:

# The return keyword
# The value or expression that the function should return

import random

def get_answer(answer_number):
    # Returns a fortune answer based on what int answer_number is, 1 to 9
   if answer_number == 1:
        return 'It is certain'
   elif answer_number == 2:
       return 'It is decidedly so'
   elif answer_number == 3:
       return 'Yes'
   elif answer_number == 4:
       return 'Reply hazy try again'
   elif answer_number == 5:
       return 'Ask again later'
   elif answer_number == 6:
       return 'Concentrate and ask again'
   elif answer_number == 7:
       return 'My reply is no'
   elif answer_number == 8:
       return 'Outlook not so good'
   elif answer_number == 9:
       return 'Very doubtful'

# The get_answer() function takes an integer argument answer_number and returns a string fortune
# based on the value of answer_number.
print('Ask a yes or no question:')
input('>')
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)