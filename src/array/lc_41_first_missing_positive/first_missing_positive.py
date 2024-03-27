class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = [n for n in nums if n > 0]
        if not nums:
            return 1
        nums.sort()
        missing = False
        temp = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > 1:
                temp = nums[i] + 1 #minimum not included
                missing = True
                break
        
        if not missing:
            temp = nums[-1] + 1
        nums = set(nums)
        for n in range(1, temp):
            if n not in nums:
                return n
        return temp