import pyperclip 

# Import the pyperclip module to copy and paste text to the clipboard.
#what is clipboard? 
# The clipboard is a temporary storage area for data that the user wants to copy from one place to another.
# For example, when you copy text from a document, it is stored in the clipboard until  
# you paste it somewhere else. The pyperclip module allows you to access the clipboard in Python.
# This program adds a bullet point to the beginning of each line in the text copied to the clipboard.
# The text is copied to the clipboard using the pyperclip module, which allows you to   
# copy and paste text to and from the clipboard.

text = pyperclip.paste() # Get the text off the clipboard.
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
    lines[i] = '* ' + lines[i] # Add a star to each string in the "lines" list.
pyperclip.copy(text)
print(text)  # Print the result on the screen too.


# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
    lines[i] = '* ' + lines[i]  # Add a star to each string in the "lines" list.
text = '\n'.join(lines)
pyperclip.copy(text) # Put the result on the clipboard.
print(text)  # Print the result on the screen too.

