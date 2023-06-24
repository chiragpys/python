# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
# occurs in the given string. String traversal will take place from left to right, not from right to left.

# Example:
# ABCDCDC
# CDC

# output
# 2


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i: i + len(sub_string)] == sub_string:
            count += 1
    return count


string = "ABCDCDC"
sub_str = 'CDC'
print(count_substring(string, sub_str))
