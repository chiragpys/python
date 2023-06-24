# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.

# Sample input
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Sample output
# False

# Explanation 0
# Set A is the strict superset of the set([1,2,3,4,5]) but not of the set([100,11,12]) because 100 is not in set A.
# Hence, the output is False.

a = set(map(int, input().split()))
flag = True
for _ in range(int(input())):
    set_n = set(map(int, input().split()))
    if not a.issuperset(set_n):
        flag = False
print(flag)



