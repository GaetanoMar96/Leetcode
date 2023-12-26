"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements 
in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        visited = set()
        l = 0
        length = len(nums)
        while l < length:
            if nums[l] in visited:
                nums.pop(l)
                length -= 1
            else:
                visited.add(nums[l])
                l += 1
        return len(nums)
        