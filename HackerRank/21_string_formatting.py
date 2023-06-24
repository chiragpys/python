# Given an integer,n, print the following values for each integer i from 1 to n:
# 1 Decimal
# 2 Octal
# 3 Hexadecimal (capitalized)
# 4 Binary

# Example:
# Input 17
# output
#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001

def print_formatted(number):
    l = len(bin(number).lstrip('0b')) + 1
    for i in range(1, number + 1):
        result = ''
        decimal = str(i).rjust(l - 1)
        octal = str(oct(i)).lstrip('0o').rjust(l)
        hexad = str(hex(i)).lstrip('0x').upper().rjust(l)
        binary = str(bin(i)).lstrip('0b').rjust(l)
        result += decimal + octal + hexad + binary
        print(result)


n = 5
print_formatted(n)
