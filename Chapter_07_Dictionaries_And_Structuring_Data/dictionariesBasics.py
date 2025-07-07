# The Dictionary Data Type
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change them after creation.
# Creating a dictionary

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["job"] = "Engineer" 
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'} 

# Modifying an existing value
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"] 
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31
# job: Engineer 

# Getting the keys and values   
print(my_dict.keys())   # Output: dict_keys(['name', 'age', 'job'])
print(my_dict.values()) # Output: dict_values(['Alice', 31, 'Engineer'])

# Getting the length of a dictionary
print(len(my_dict))  # Output: 3    

# Copying a dictionary
my_dict_copy = my_dict.copy()   
print(my_dict_copy)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Nested dictionaries
nested_dict = {
    "person": {
        "name": "Bob",
        "age": 25
    },
    "address": {
        "city": "Los Angeles",
        "state": "CA"
    }
}

# Accessing nested dictionary values
print(nested_dict["person"]["name"])  # Output: Bob 
print(nested_dict["address"]["city"])  # Output: Los Angeles

# Adding a new key-value pair to a nested dictionary
nested_dict["person"]["job"] = "Designer"
print(nested_dict)  
# Output: {'person': {'name': 'Bob', 'age': 25, 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'CA'}}

# Modifying a value in a nested dictionary
nested_dict["address"]["state"] = "NY"  
print(nested_dict)
# Output: {'person': {'name': 'Bob', 'age': 25, 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'NY'}}

# Removing a key-value pair from a nested dictionary
del nested_dict["person"]["age"]
print(nested_dict)
# Output: {'person': {'name': 'Bob', 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'NY'}}

# Checking if a key exists in a nested dictionary
if "job" in nested_dict["person"]:
    print("Job exists in the nested dictionary")  # Output: Job exists in the nested dictionary

# Iterating through a nested dictionary
for outer_key, outer_value in nested_dict.items():
    print(f"{outer_key}:") # Output: person: Output: address:
    for inner_key, inner_value in outer_value.items(): 
        print(f"  {inner_key}: {inner_value}")  

# Output:
# person:       
# name: Bob
# job: Designer 
# address:
# city: Los Angeles
# state: NY

# Getting the keys and values of a nested dictionary
print(nested_dict.keys())   # Output: dict_keys(['person', 'address'])  
print(nested_dict.values()) 
# Output: dict_values([{'name': 'Bob', 'job': 'Designer'}, {'city': 'Los Angeles', 'state': 'NY'}]) 

# Getting the length of a nested dictionary
print(len(nested_dict))  # Output: 2

# Copying a nested dictionary
nested_dict_copy = nested_dict.copy()   
print(nested_dict_copy)
# Output: {'person': {'name': 'Bob', 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'NY'}}

# Clearing a nested dictionary
nested_dict.clear() 
print(nested_dict)  # Output: {}

# Dictionary methods
# get() - Returns the value for a specified key, or a default value if the key does not exist
print(my_dict_copy.get("name", "Not Found"))  # Output: Alice   
print(my_dict_copy.get("salary", "Not Found"))  # Output: Not Found 

# items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(my_dict_copy.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])    

# keys() - Returns a view object that displays a list of all the keys in the dictionary
print(my_dict_copy.keys())  # Output: dict_keys(['name', 'age', 'job'])

# values() - Returns a view object that displays a list of all the values in the dictionary 
print(my_dict_copy.values())  # Output: dict_values(['Alice', 31, 'Engineer'])  

# pop() - Removes the specified key and returns the corresponding value
print(my_dict_copy.pop("age", "Not Found"))  # Output: 31   

# popitem() - Removes and returns the last inserted key-value pair
print(my_dict_copy.popitem())  # Output: ('job', 'Engineer')    

# update() - Updates the dictionary with the specified key-value pairs
my_dict_copy.update({"city": "San Francisco", "country": "USA"})
print(my_dict_copy)
# Output: {'name': 'Alice', 'city': 'San Francisco', 'country': 'USA'}  

# fromkeys() - Creates a new dictionary with specified keys and a default value
new_dict = dict.fromkeys(["a", "b", "c"], 0)    
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0} 

# setdefault() - Returns the value of a key if it exists, otherwise inserts the key with a specified value
print(my_dict_copy.setdefault("name", "Default Name"))  # Output: Alice 
print(my_dict_copy.setdefault("age", 25))  # Output: 25 (adds 'age' key with value 25)
print(my_dict_copy) # Output: {'name': 'Alice', 'city': 'San Francisco', 'country': 'USA', 'age': 25}

# clear() - Removes all items from the dictionary
my_dict_copy.clear()    
print(my_dict_copy)  # Output: {}   

# Dictionary comprehensions
# Creating a dictionary using a comprehension   
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering a dictionary using a comprehension
filtered_dict = {k: v for k, v in squared_dict.items() if v > 5}
print(filtered_dict)  # Output: {3: 9, 4: 16}   

# Merging dictionaries
dict1 = {"a": 1, "b": 2}    
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # Merges dict1 and dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}  # Note: 'b' from dict2 overwrites 'b' from dict1    

# Using the | operator to merge dictionaries (Python 3.9+)
merged_dict_v2 = dict1 | dict2  
print(merged_dict_v2)  # Output: {'a': 1, 'b': 3, 'c': 4}  # Note: 'b' from dict2 overwrites 'b' from dict1 

# Using the update() method to merge dictionaries
dict1.update(dict2) 
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}  # Note: 'b' from dict2 overwrites 'b' from dict1

# Using the union() method to merge dictionaries (Python 3.9+)
dict3 = {"d": 5, "e": 6}    
dict4 = {"e": 7, "f": 8}
merged_dict_v3 = dict3 | dict4
print(merged_dict_v3)  # Output: {'d': 5, 'e': 7, 'f': 8}  # Note: 'e' from dict4 overwrites 'e' from dict3 

# Using the union() method with a list of dictionaries
dicts_list = [dict1, dict2, dict3, dict4]   
merged_dict_v4 = {}
for d in dicts_list:
    merged_dict_v4 |= d  # Merges each dictionary in the list   
print(merged_dict_v4)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  # Note: 'b' from dict2 and 'e' 
# from dict4 overwrite previous values  

# Using the union() method with a set of dictionaries
dicts_set = {dict1, dict2, dict3, dict4}    
merged_dict_v5 = {}
for d in dicts_set:
    merged_dict_v5 |= d  # Merges each dictionary in the set    
print(merged_dict_v5)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  # Note: 'b' from dict2 and 'e' 
# from dict4 overwrite previous values  


# Using the union() method with a dictionary comprehension
merged_dict_v6 = {k: v for d in dicts_list for k, v in d.items()}
print(merged_dict_v6)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  # Note: 'b' from dict2 and 'e' 
# from dict4 overwrite previous values  

# Using the union() method with a generator expression
merged_dict_v7 = {k: v for d in (dict1, dict2, dict3, dict4) for k, v in d.items()}
print(merged_dict_v7)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  # Note: 'b' 
# from dict2 and 'e' from dict4 overwrite previous values  

# Using the union() method with a list comprehension
merged_dict_v8 = {k: v for d in [dict1, dict2, dict3, dict4] for k, v in d.items()}
print(merged_dict_v8)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  
# # Note: 'b' from dict2 and 'e' from dict4 overwrite previous values      

# Using the union() method with a set comprehension
merged_dict_v9 = {k: v for d in {dict1, dict2,  dict3, dict4} for k, v in d.items()}
print(merged_dict_v9)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  
# # Note: 'b' from dict2 and 'e' from dict4 overwrite previous values      

# Using the union() method with a dictionary union operator
merged_dict_v10 = dict1 | dict2 | dict3 | dict4     
print(merged_dict_v10)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  # Note: 'b' 
# from dict2 and 'e' from dict4 overwrite previous values 

# Using the union() method with a dictionary union operator and a list of dictionaries
merged_dict_v11 = {}    
for d in [dict1, dict2, dict3, dict4]:
    merged_dict_v11 |= d  # Merges each dictionary in the list  
print(merged_dict_v11)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  
# # Note: 'b' from dict2 and 'e' from dict4 overwrite previous values 

# Using the union() method with a dictionary union operator and a set of dictionaries
merged_dict_v12 = {}    
for d in {dict1, dict2, dict3, dict4}:
    merged_dict_v12 |= d  # Merges each dictionary in the set
print(merged_dict_v12)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  
# # Note: 'b' from dict2 and 'e' from dict4 overwrite previous values 

# Using the union() method with a dictionary union operator and a generator expression
merged_dict_v13 = {}        
for d in (dict1, dict2, dict3, dict4):
    merged_dict_v13 |= d  # Merges each dictionary in the generator expression
print(merged_dict_v13)  
# Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 7, 'f': 8}  
# # Note: 'b' from dict2 and 'e' from dict4 overwrite previous values 



