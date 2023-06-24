# Task
# The students of District College have subscriptions to English and French newspapers. Some students have
# subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers. You
# are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is
# subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number
# of students who have subscribed to at least one newspaper.

# input sample
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# output sample
# 13

n= int(input())
enroll_english=set(map(int,input().split()))
b= int(input())
enroll_french=set(map(int,input().split()))
enroll_atleastone=enroll_english.union(enroll_french)
print(len(enroll_atleastone))



