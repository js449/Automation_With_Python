import pyperclip

readme_text = """
## 📘 Chapter 8: Strings and Text Editing

### 🔍 Overview
Chapter 8 teaches how to work with **text data** in Python. You’ll learn how to manipulate, search, and format strings using various string methods, regular expressions, and clipboard operations with `pyperclip`.

---

### 🧠 Key Concepts
- **String methods**: `upper()`, `lower()`, `isalpha()`, `startswith()`, `join()`, `split()`, `strip()`, etc.
- **String slicing**: Access specific characters or substrings.
- **Clipboard automation**: Using `pyperclip` to copy/paste text.
- **Text editing automation**: Add bullets, format lines, clean up text.
- **String immutability**: Understanding how strings behave when modified.

---

### 📦 Python Modules Used
- `pyperclip` — to interact with the system clipboard
- `re` (covered later) — for more advanced pattern matching (optional for now)

---

### 🧪 Practice Ideas
- Add `*` or `-` to the beginning of each line from clipboard text.
- Convert a list of comma-separated names into a bulleted list.
- Strip extra spaces and format messy input text.
- Write a script to censor specific words in a paragraph.

---

### 🛠️ Example Mini Project: Bullet Point Adder
```python
import pyperclip

text = pyperclip.paste()
lines = text.split('\\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\\n'.join(lines)
pyperclip.copy(text)
print("Updated text copied to clipboard:")
print(text)

