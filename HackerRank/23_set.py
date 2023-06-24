# A set is an unordered collection of elements without duplicate entries. When printed, iterated or converted into a
# sequence, its elements will appear in an arbitrary order. Basically, sets are used for membership testing and
# eliminating duplicate entries.
# Task
# Now, let's use our knowledge of sets and help Mickey. Ms. Gabriel Williams is a
# botany professor at District College. One day, she asked her student Mickey to compute the average of all the
# plants with distinct heights in her greenhouse.

# sample input
# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

# sample output
# 169.375

def average(array):
    array = set(array)
    avg = sum(array) / len(array)
    return avg


n = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174,]
result = average(n)
print(result)
