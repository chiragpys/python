# You are given a string 'S' and width 'w'.
# Your task is to wrap the string into a paragraph of width 'w'.

# Example
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4
result = wrap(s, w)
print(result)

# textwrap wrap method
print(textwrap.wrap(s,4))

