# Task
# You have a non-empty set S, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.

# Sample input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

# sample output
# 4

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))