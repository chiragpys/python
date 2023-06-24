# 1. Two Sum

# Example:1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example:2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example:3
# Input: nums = [3,3], target = 6
# Output: [0,1]

# a = []
# length = len(nums) - 1
# for i in range(length):
#     if nums[i] + nums[i+1] == target:
#         a.extend([i, i+1])
# print(a)

def two_sum(num, targets):
    length = len(num) - 1
    for i in range(length):
        if num[i] + num[i + 1] == targets:
            return [i, i + 1]


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))
