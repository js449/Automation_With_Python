# 📘 Chapter: Dictionaries in Python

This chapter introduces **dictionaries**, a powerful data structure in Python used to store data in **key-value pairs**. Unlike lists (which are ordered and use indexes), dictionaries are unordered and use keys to access values.

---

## 🧠 What I Learned

- **Dictionaries** store data as `{key: value}` pairs.
- Keys must be **unique and immutable** (strings, numbers, tuples).
- Values can be any data type.
- They are **unordered** (prior to Python 3.7).

---

## 🔑 Key Concepts

| Concept | Example |
|--------|---------|
| Create a dictionary | `my_cat = {'size': 'fat', 'color': 'gray'}` |
| Access a value by key | `my_cat['size']` → `'fat'` |
| Add new key-value pair | `my_cat['age'] = 3` |
| Check for key existence | `'color' in my_cat` |
| Delete a key | `del my_cat['size']` |
| Use `.get()` safely | `my_cat.get('breed', 'unknown')` |
| Loop through items | `for key, value in my_cat.items():` |
| Keys only | `my_cat.keys()` |
| Values only | `my_cat.values()` |

---

## 🛠️ Practice Exercises

- Created a program that counts the frequency of each letter in a string.
- Wrote a character inventory counter (like in a game).
- Used `.get()` to avoid key errors when checking user input.

---

## 🧪 Code Sample

```python
message = 'hello world'
count = {}

for char in message:
    count[char] = count.get(char, 0) + 1

print(count)
