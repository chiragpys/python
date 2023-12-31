# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Sample input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample output
# True
# False
# False

T = int(input())
for i in range(T):
    a = int(input())
    myset_A = set(map(int,input().split()))
    b = int(input())
    myset_B = set(map(int,input().split()))
    if myset_A.issubset(myset_B):
        print("True")
    else:
        print("False")
