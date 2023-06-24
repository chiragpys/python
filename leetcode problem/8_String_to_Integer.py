# 8. String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s
# atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.

# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is
# either. This determines if the final result is negative or positive respectively. Assume the result is positive if
# neither is present.

# Read in next the characters until the next non-digit character or the end of the input is
# reached. The rest of the string is ignored.

# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
# If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
# Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be
# clamped to 231 - 1.

# Return the integer as the final result.

# Example 1:
# Input: s = "42"
# Output: 42

# Example 2:
# Input: s = "   -42"
# Output: -42

# Example 3:
# Input: s = "4193 with words"
# Output: 4193

class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        val = -1 if s[0] == '-' else 1

        if s[0] in ('-', '+'):
            s = s[1:]

        num = 0

        for i in s:
            if not i.isdigit():
                break
            num = num * 10 + int(i)
            if val * num <= -2 ** 31:
                return -2 ** 31
            if val * num >= 2 ** 31 - 1:
                return 2 ** 31 - 1

        return val * num

s = '   -42 with word'
str1 = Solution()
result = str1.myAtoi(s)
print(result)

