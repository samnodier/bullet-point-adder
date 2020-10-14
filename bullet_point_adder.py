#!python3
# bullet_point_adder.py - Adds a stars to the beginning of every line
# of the text from the clipboard

# import module first
import pyperclip

# get the text from clipboard
text = pyperclip.paste()

# Separate the lines and add stars at the beginning
lines = text.split('\n')
for i in range(len(lines)):         # Loop through all indexes in range of length of the list
    lines[i] = '*  ' + lines[i]     # add a star and two spaces to each string in the list


# Join the text again
text = '\n'.join(lines)

# Put the text back into the clipboard
pyperclip.copy(text)

