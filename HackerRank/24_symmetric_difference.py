# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# sample input
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}

# sample output
# 5
# 9
# 11
# 12

M = int(input("Enter a integer M: "))
a = [input("Enter a number: ") for _ in range(M)]
# a = list(map(int, input().split()))
N = int(input("Enter a integer N: "))
b = [input("Enter a number: ") for _ in range(N)]
# b = list(map(int, input().split()))
a = set(a)
b = set(b)
c =a.symmetric_difference(b)
for i in sorted(c):
    print(i)

    