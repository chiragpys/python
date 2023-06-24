# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
# letters and vice versa.

# Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonista 2 → pYTHONIST 2

def swap_case(s):
    new_str = ""
    for i in s:
        if i.islower():
            new_str += i.upper()
        elif i.isupper():
            new_str += i.lower()
        else:
            new_str += i
    return new_str


s = 'Pythonista 2'
result = swap_case(s)
print(result)


