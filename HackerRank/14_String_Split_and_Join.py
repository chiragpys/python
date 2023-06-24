# In Python, a string can be split on a delimiter.

# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string

# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a


s = "this is a string"
result = split_and_join(s)
print(result)

