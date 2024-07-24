sentence = input("Enter a sentence: ")
char_to_replace = input("Enter a character to replace: ")
new_char = input("Enter the new character: ")

# Create a new string with the replacements
new_sentence = ""
for c in sentence:
    if c != char_to_replace:
        new_sentence += c
    else:
        new_sentence += new_char

# Print the modified sentence
print("Modified sentence:", new_sentence)
