# 7 Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x):
        s = str(abs(x))
        rev = int(s[::-1])

        if rev > 2147483647:
            return 0

        if x > 0:
            return rev
        else:
            return (rev * -1)
x = 123
r = Solution()
r = r.reverse(x)
print(r)
