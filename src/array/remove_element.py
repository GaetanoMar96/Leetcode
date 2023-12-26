"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, 
you need to do the following things:

Change the array nums such that the first k elements of nums contain 
the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        ptr1 = 0
        last = len(nums)
        while ptr1 < last:
            if nums[ptr1] == val:
                for i in range(ptr1, last-1):
                    nums[i] = nums[i+1]    
                last-=1
            else:
                ptr1+=1
            
        return last
    