"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1, pt2 = 0, 0
        while pt1 < m and pt2 < n:
            if nums1[pt1] > nums2[pt2]:
                temp = nums2[pt2]
                nums2[pt2] = nums1[pt1] 
                nums1[pt1] = temp
                nums2.sort()
            pt1 += 1
        for i in range(len(nums2)):
            nums1[m+i] = nums2[i]

        