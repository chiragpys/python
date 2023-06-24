# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from statistics import median

# Solution: 1
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        return median(nums1)

# Solution: 2
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         for i in nums2:
#             nums1.append(i)
#         nums1.sort()
#         n = len(nums1)//2
#
#         if len(nums1) %2 == 0:
#             return (nums1[n-1]+nums1[n])/2
#         else:
#             return nums1[n]