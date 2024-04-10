from collections import defaultdict
class Solution:

    #For each valid window, we can calculate the total number of subarrays it can form using the formula right - left + 1. 
    #This represents the number of subarrays ending at the current element (right) 
    #and starting anywhere from the current left boundary (left) to the right pointer (right) (inclusive).
    #The calculation right - left + 1, counts the subarrays with at most k distinct integers.
    #After calculating the total count of subarrays with distinct integers less than or equal to k using slidingWindowAtMost(nums, k), we need to isolate the subarrays that strictly meet the target k.
    #This can be achieved by subtracting the total count of subarrays with distinct integers less than k (slidingWindowAtMost(nums, k - 1)) from the total count obtained earlier. 
    #By subtracting the latter from the former, we essentially remove the subarrays that don't reach k and are left with only the subarrays that have exactly k distinct integers
    #Time complexity O(N), Space complexity O(N) for the hashmap
    
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def countsubarray(k: int) -> int:
            count = defaultdict(int)
            l = 0
            res = 0
            for r in range(len(nums)):
                count[nums[r]] += 1
                while l < len(nums) and len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                #proceed to count
                res += r - l + 1
            return res
        return countsubarray(k) - countsubarray(k-1)