# Chapter 5 -     Lists


# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[0])  # Accessing the first item in the list
# print(spam[1])  # Accessing the second item in the list
# print(spam[-1])  # Accessing the third item in the list

# spam = [ ['cat', 'bat'], ['rat', 'elephant']]
# print(spam[0][0])  # Accessing the first item in the first sublist
# print(spam[1][1])  # Accessing the second item in the second sub
# print(spam[0][-1])  # Accessing the second item in the first sublist

# Lists can be sliced to get a sublist.
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:2])  # Slicing the list to get the first two items
print(spam[1:3])  # Slicing the list to get the second and third items
print(spam[:2])   # Slicing the list to get the first two items


# Lists can be concatenated using the + operator.
spam1 = ['cat', 'bat']
spam2 = ['rat', 'elephant']
spam3 = spam1 + spam2  # Concatenating two lists
print(spam3)  # Output: ['cat', 'bat', 'rat', 'elephant']

# Lists can be repeated using the * operator.
spam4 = spam1 * 2  # Repeating the list twice   
print(spam4)  # Output: ['cat', 'bat', 'cat', 'bat']

# Lists can be modified by adding or removing items.
spam5 = ['cat', 'bat', 'rat']   
spam5.append('elephant')  # Adding an item to the end of the list
print(spam5)  # Output: ['cat', 'bat', 'rat', 'elephant']

spam5.remove('bat')  # Removing an item from the list
print(spam5)  # Output: ['cat', 'rat', 'elephant']  

# Lists can be extended using the extend() method.
spam5.extend(['dog', 'fish'])  # Adding multiple items to the end of the list
print(spam5)  # Output: ['cat', 'rat', 'elephant', 'dog', 'fish']

# Lists can be inserted at a specific index using the insert() method.
spam5.insert(1, 'bat')  # Inserting 'bat' at index 1
print(spam5)  # Output: ['cat', 'bat', 'rat', 'elephant', 'dog', 'fish']

# Lists can be removed using the pop() method.
spam6 = ['cat', 'bat', 'rat', 'elephant']       
removed_item = spam6.pop()  # Removing the last item from the list
print(removed_item)  # Output: elephant  # The item that was removed    
print(spam6)  # Output: ['cat', 'bat', 'rat']  # The list after removal

# Lists can be counted using the count() method.
spam7 = ['cat', 'bat', 'rat', 'elephant', 'cat']    
count_cat = spam7.count('cat')  # Counting the occurrences of 'cat'
print(count_cat)  # Output: 2  # The number of times 'cat' appears in the list

# Lists can be found using the index() method.
spam8 = ['cat', 'bat', 'rat', 'elephant']           
index_of_rat = spam8.index('rat')  # Finding the index of 'rat'
print(index_of_rat)  # Output: 2  # The index of 'rat'

# Lists can be checked for emptiness using the len() function.
spam9 = []  # An empty list 
print(len(spam9) == 0)  # Checking if the list is empty
# Output: True  # The list is empty

# Lists can be checked for length using the len() function.
spam10 = ['cat', 'bat', 'rat', 'elephant']
print(len(spam10))  # Getting the length of the list
# Output: 4  # The number of items in the list

#delete can be used to remove an item from a list.
spam11 = ['cat', 'bat', 'rat', 'elephant']
del spam11[1]  # Deleting the item at index 1
print(spam11)  # Output: ['cat', 'rat', 'elephant']

# Lists can be sorted using the sort() method.
spam6 = ['cat', 'bat', 'rat', 'elephant']   
spam6.sort()  # Sorting the list in ascending order
print(spam6)  # Output: ['bat', 'cat', 'elephant', 'rat']   

# Lists can be reversed using the reverse() method.
spam7 = ['cat', 'bat', 'rat', 'elephant']       
spam7.reverse()  # Reversing the order of the list
print(spam7)  # Output: ['elephant', 'rat', 'bat', 'cat']   

# Lists can be cleared using the clear() method.
spam8 = ['cat', 'bat', 'rat', 'elephant']   
spam8.clear()  # Clearing the list
print(spam8)  # Output: []  # The list is now empty 

# Lists can be copied using the copy() method.
spam9 = ['cat', 'bat', 'rat', 'elephant']
spam10 = spam9.copy()  # Copying the list
print(spam10)  # Output: ['cat', 'bat', 'rat', 'elephant']

# Lists can be checked for membership using the in operator.
spam11 = ['cat', 'bat', 'rat', 'elephant']  
print('cat' in spam11)  # Checking if 'cat' is in the list
print('dog' in spam11)  # Checking if 'dog' is in the list      

# Lists can be iterated over using a for loop.
spam12 = ['cat', 'bat', 'rat', 'elephant']
for item in spam12:
    print(item)  # Output: cat, bat, rat, elephant (each on a new line)

# Lists can be used to store mixed data types.
spam13 = ['cat', 42, 3.14, True]  # A list with mixed data types
print(spam13)  # Output: ['cat', 42, 3.14, True]    

# Lists can be nested, meaning you can have lists within lists.
spam14 = [['cat', 'bat'], ['rat', 'elephant']]  # A nested list
print(spam14)  # Output: [['cat', 'bat'], ['rat', 'elephant']]  

# Lists can be used to store collections of data, such as names, numbers, or objects.
names = ['Alice', 'Bob', 'Charlie']  # A list of names
numbers = [1, 2, 3, 4, 5]  # A list of numbers
objects = ['apple', 'banana', 'cherry']  # A list of objects    

# Lists can be used to store data that needs to be processed in a specific order.
tasks = ['task1', 'task2', 'task3']  # A list of tasks
for task in tasks:
    print(f'Processing {task}')  # Output: Processing task1, Processing task2, Processing task3 (each on a new line)   

# List Item Enumeration
# Lists can be enumerated to get both the index and the item.
spam15 = ['cat', 'bat', 'rat', 'elephant']  
for index, item in enumerate(spam15):
    print(f'Index: {index}, Item: {item}')
# Output:
# Index: 0, Item: cat
# Index: 1, Item: bat
# Index: 2, Item: rat   
# Index: 3, Item: elephant


# random.shuffle() can be used to shuffle the items in a list.
import random       
spam16 = ['cat', 'bat', 'rat', 'elephant']
random.shuffle(spam16)  # Shuffling the list    
print(spam16)  # Output: The items in the list are now shuffled in random order

# random.choice() can be used to select a random item from a list.
random_item = random.choice(spam16)  # Selecting a random item from the list    
print(random_item)  # Output: A random item from the list, e.g., 'bat'

# random.sample() can be used to select a random sample of items from a list.
random_sample = random.sample(spam16, 2)  # Selecting a random sample of 2 items from the list
print(random_sample)  # Output: A random sample of 2 items from the list, e.g., ['rat', 'elephant']



