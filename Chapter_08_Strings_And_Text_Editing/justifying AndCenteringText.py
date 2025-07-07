# Justifying and Centering Text
# This code provides functions to justify and center text within a specified width.
# The `justify_text` function splits the text into words and arranges them into lines that
# fit within the specified width, adding spaces as necessary to justify the text.
# The `center_text` function centers each line of text within the specified width.
# The example usage demonstrates how to use these functions with a sample text and a specified width.
# The justified text is left-aligned, while the centered text is centered within the specified width.
# The output is printed to the console. 

def justify_text(text, width):
    """
    Justify the text to a specified width.
    
    :param text: The text to justify.
    :param width: The width to justify the text to.
    :return: Justified text.
    """
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line).ljust(width))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line).ljust(width))

    return '\n'.join(lines)

def center_text(text, width):
    """
    Center the text to a specified width.
    
    :param text: The text to center.
    :param width: The width to center the text to.
    :return: Centered text.
    """
    lines = []
    for line in text.split('\n'):
        lines.append(line.center(width))
    return '\n'.join(lines)

# Example usage
if __name__ == "__main__":  
    sample_text = "This is an example of justifying and centering text in Python."
    width = 40

    justified_text = justify_text(sample_text, width)
    centered_text = center_text(sample_text, width)

    print("Justified Text:\n")
    print(justified_text)
    print("\nCentered Text:\n")
    print(centered_text)        


