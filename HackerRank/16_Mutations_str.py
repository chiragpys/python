# Task
# Read a given string, change the character at a given index and then print the modified string.

# Example:
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'

# Output
# abrackdabra

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string


s = input("Enter a string: ")
i, c = input("You have enter first position and character:").split()
s_new = mutate_string(s, int(i), c)
print(s_new)
