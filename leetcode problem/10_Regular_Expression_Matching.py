# 10. Regular Expression Matching

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 2:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

import re


class Solution:
    def isMatch(self, s, p):
        s = s.lower()
        p = p.lower()

        if not p:
            return not p

        match = re.match(p, s)

        if match:
            return True
        else:
            return False


s = "ab"
p = ".*"

reg = Solution()

result = reg.isMatch(s, p)
print(result)
