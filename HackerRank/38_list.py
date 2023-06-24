# Consider a list (list = []). You can perform the following commands:
# 1 insert i e: Insert integer  at position .
# 2 print: Print the list.
# 3 remove e: Delete the first occurrence of integer .
# 4 append e: Insert integer  at the end of the list.
# 5 sort: Sort the list.
# 6 pop: Pop the last element from the list.
# 7 reverse: Reverse the list.

# Sample input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


N = int(input())
commands = []
list_ = []

for i in range(0, N):
    command = input()
    commands.append(command)

for command in commands:
    if command.split()[0] == "insert":
        list_.insert(int(command.split()[1]), int(command.split()[2]))
    elif command.split()[0] == "print":
        print(list_)
    elif command.split()[0] == "remove":
        list_.remove(int(command.split()[1]))
    elif command.split()[0] == "append":
        list_.append(int(command.split()[1]))
    elif command.split()[0] == "sort":
        list_.sort()
    elif command.split()[0] == "pop":
        list_.pop()
    elif command.split()[0] == "reverse":
        list_.reverse()
