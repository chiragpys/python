# Task
# You are given a string S.
# Your task is to find out if the string  contains S: alphanumeric characters,
# alphabetical characters, digits, lowercase and uppercase characters

# Output Format
# In the first line, print True if 'S' has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if 'S' has any alphabetical characters. Otherwise, print False.
# In the third line, print True if 'S' has any digits. Otherwise, print False.
# In the fourth line, print True if 'S' has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if 'S' has any uppercase characters. Otherwise, print False.

def string_validators(s):
    answer = [False, False, False, False, False]
    for i in s:
        if i.isalnum() == True:
            answer[0] = True
        if i.isalpha() == True:
            answer[1] = True
        if i.isdigit() == True:
            answer[2] = True
        if i.islower() == True:
            answer[3] = True
        if i.isupper() == True:
            answer[4] = True

    for i in answer:
        print(i)


s = 'qA2'
string_validators(s)
