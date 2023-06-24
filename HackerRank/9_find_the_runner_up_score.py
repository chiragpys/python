# Given the participants' scoresheet for your University Sports Day, you are required to find the runner-up score.
# You are given 'n' scores. Store them in a list and find the score of the runner-up.

# Example:
# 5
# 2 3 6 6 5
# Given list is[2,3,6,6,5] . The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score.
# output
# 5

n = int(input("Enter a number:"))
arr = map(int, input("Enter an integers separated by a space:").split())
l = list(arr)
print(sorted(set(l), reverse=True)[1])



