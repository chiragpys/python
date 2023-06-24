# Input Format
# The first line consists of an integer,K, the size of each group.
# The second line contains the unordered elements of the room number list.

# Sample input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

# Sample output
# 8

# Explanation The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the
# given list, all of the numbers repeat 5 times except for room number8 .
# Hence, 8 is the Captain's room number.


# K = int(input())
# Rooms = (list(input().split()))
Rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
setRooms = set(Rooms)
print(setRooms)
for x in setRooms:
    Rooms.remove(x)
print(set(Rooms))
setRooms.difference_update(set(Rooms))
print(setRooms.pop())
