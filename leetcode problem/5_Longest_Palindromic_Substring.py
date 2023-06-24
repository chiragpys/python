# 5 Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                word = s[i:j]
                if word == word[::-1]:
                    if len(word) > len(longest):
                        longest = word

        return longest
s = "babad"
string = Solution()

print(string.longestPalindrome(s))

