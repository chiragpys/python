# 12. Integer to Roman

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.


# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def intToRoman(self, num: int) -> str:
        numlist = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romlist = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        rom = ''
        while num:
            div = num // numlist[i]
            num %= numlist[i]

            while div:
                rom += romlist[i]
                div -= 1
            i -= 1
        return rom

num = 2

rom = Solution()
result = rom.intToRoman(num)
print(result)
