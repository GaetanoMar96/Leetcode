class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length

        pre = 1
        for i in range(length):
            res[i] *= pre
            pre *= nums[i]
        
        # all products except with the last one
        post = 1
        for i in range(length -1,-1,-1):
            res[i] *= post
            post *= nums[i] #multiply all except self
        return res