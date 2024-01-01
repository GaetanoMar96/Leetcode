class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = set()
        res = []
        def twoSum(idx, target):
            hashmap = {}
            for i in range(len(nums)):
                if i == idx:
                    continue
                if nums[i] in hashmap:
                    r = [nums[i], -target, target - nums[i]]
                    r.sort()
                    temp = (r[0],r[1],r[2])
                    if temp not in sol:
                        sol.add(temp)
                        res.append(r)
                    
                hashmap[target - nums[i]] = True
            
        
        for i, num in enumerate(nums):
            twoSum(i, -num)
        return res