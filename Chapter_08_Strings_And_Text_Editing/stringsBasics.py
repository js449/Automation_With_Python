# STRINGS AND TEXT EDITING  
# Strings are immutable sequences of characters
# They can be created using single quotes, double quotes, or triple quotes

# Example of creating strings
single_quote_string = 'Hello, World!'   
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello, World!'''  # Triple quotes allow for multi-line strings
triple_quote_string_multiline = """This is a multi-line string
that spans multiple lines."""   
# Strings can contain any character, including special characters
special_char_string = 'This string contains a newline character\nand a tab character\t.'    

#Raw strings can be created using the r prefix to avoid escape sequences
raw_string = r'This is a raw string with a newline character \n and a tab character \t.'    

#F strings (formatted string literals) can be created using the f prefix
name = "Alice"  
age = 30
f_string = f"My name is {name} and I am {age} years old."  # Allows embedding expressions inside string literals    

# %s is used for string formatting in previous versions of Python
percent_string = "My name is %s and I am %d years old." % (name, age)  
# %s is replaced by the string value of name, %d by the integer value of age 

#formatted strings can also be created using the format() method in previous versions of Python
formatted_string = "My name is {} and I am {} years old.".format(name, age) 

# Strings can be concatenated using the + operator
concatenated_string = single_quote_string + " " + double_quote_string   

# Strings can be repeated using the * operator
repeated_string = single_quote_string * 3  # Repeats the string three times

# Strings can be indexed and sliced
first_character = single_quote_string[0]  # Accessing the first character
substring = single_quote_string[0:5]  # Slicing the first five characters

# Negative indexing allows access from the end of the string
last_character = single_quote_string[-1]  # Accessing the last character    

# Strings can be iterated over
for char in single_quote_string:
    print(char, end=' ')  # Prints each character in the string 
print()  # Newline after printing all characters    

# Strings can be checked for membership using the 'in' operator
is_hello_in_string = 'Hello' in single_quote_string  # Returns True if 'Hello' is in the string 

# Strings can be formatted using f-strings (Python 3.6+)
name = "Alice"  
age = 30
formatted_string = f"My name is {name} and I am {age} years old."

# Strings can also be formatted using the format() method
formatted_string_method = "My name is {} and I am {} years old.".format(name, age) 


# Strings can be split into a list of substrings using the split() method
split_string = single_quote_string.split(", ")  # Splits the string at the comma and space  

# Strings can be joined using the join() method
joined_string = ", ".join(split_string)  # Joins the list of substrings with a comma and space  

# Strings can be stripped of leading and trailing whitespace using the strip() method
stripped_string = "   Hello, World!   ".strip()  # Removes leading and trailing whitespace  

# Strings can be converted to uppercase or lowercase
uppercase_string = single_quote_string.upper()  # Converts the string to uppercase  
lowercase_string = single_quote_string.lower()  # Converts the string to lowercase  

# Strings can be checked for equality
is_equal = single_quote_string == double_quote_string  # Returns True if the strings are equal 

# Strings can be checked for inequality
is_not_equal = single_quote_string != double_quote_string  # Returns True if the strings are not equal  

# Strings can be checked for starting or ending with a specific substring
starts_with_hello = single_quote_string.startswith("Hello")  # Returns True if the string starts with "Hello"
ends_with_world = single_quote_string.endswith("World!")  # Returns True if the string ends with "World!"   

# Strings can be counted for occurrences of a substring
count_hello = single_quote_string.count("Hello")  # Counts the occurrences of "Hello" in the string 

# Strings can be replaced using the replace() method
replaced_string = single_quote_string.replace("World", "Python")  # Replaces "World" with "Python" in the string  

# Strings can be checked for alphanumeric characters
is_alphanumeric = single_quote_string.isalnum()  # Returns True if the string is alphanumeric 
                                                 #(contains only letters and numbers)
# Strings can be checked for alphabetic characters  
is_alpha = single_quote_string.isalpha()  # Returns True if the string contains only alphabetic characters

# Strings can be checked for numeric characters 
is_numeric = single_quote_string.isnumeric()  # Returns True if the string contains only numeric characters 

# Strings can be checked for whitespace characters
is_space = single_quote_string.isspace()  # Returns True if the string contains only whitespace characters

# Strings can be checked for digits
is_digit = single_quote_string.isdigit()  # Returns True if the string contains only digits 

# Strings can be checked for printable characters
is_printable = single_quote_string.isprintable()  # Returns True if the string contains only printable characters   

# Strings can be checked for lowercase characters
is_lower = single_quote_string.islower()  # Returns True if the string contains only lowercase characters   

# Strings can be checked for uppercase characters
is_upper = single_quote_string.isupper()  # Returns True if the string contains only uppercase characters

# Strings can be checked for title case
is_title = single_quote_string.istitle()  # Returns True if the string is in title case 
                                            #(first letter of each word is uppercase)    
# Strings can be checked for a specific character
contains_a = 'a' in single_quote_string  # Returns True if the string contains the character 'a'    

# Strings can be checked for a specific substring
contains_hello = 'Hello' in single_quote_string  # Returns True if the string contains the substring 'Hello'

# Strings can be checked for a specific character at a specific index
is_first_char_h = single_quote_string[0] == 'H'  # Returns True if the first character is 'H'   

# Strings can be checked for a specific substring at the start
starts_with_hello = single_quote_string.startswith('Hello')  # Returns True if the string starts with 'Hello'   

# Strings can be checked for a specific substring at the end
ends_with_world = single_quote_string.endswith('World!')  # Returns True if the string ends with 'World!'

# Strings can be checked for a specific substring in a case-insensitive manner
contains_hello_case_insensitive = 'hello' in single_quote_string.lower()  # Returns True if 'hello' is in the string,
                                                                          #ignoring case 
# Strings can be checked for a specific substring in a case-sensitive manner
contains_hello_case_sensitive = 'Hello' in single_quote_string  # Returns True if 'Hello' is in the string,
                                                                #considering case    

# Strings can be checked for a specific character in a case-insensitive manner
contains_a_case_insensitive = 'a' in single_quote_string.lower()  # Returns True if 'a' is in the string,
                                                                      #ignoring case        
# Strings can be checked for a specific character in a case-sensitive manner
contains_a_case_sensitive = 'a' in single_quote_string  # Returns True if 'a' is in the string,
                                                              #considering case 

# Strings can be checked for a specific character at a specific index in a case-insensitive manner
is_first_char_h_case_insensitive = single_quote_string[0].lower() == 'h'  # Returns True if the first character is 'h',
                                                                          #ignoring case
# Strings can be checked for a specific character at a specific index in a case-sensitive manner
is_first_char_h_case_sensitive = single_quote_string[0] == 'H'  # Returns True if the first character is 'H',
                                                                  #considering case
# Strings can be checked for a specific substring at the start in a case-insensitive manner
starts_with_hello_case_insensitive = single_quote_string.lower().startswith('hello')  # Returns True if the string starts with 'hello',
                                                                                  #ignoring case

