#Tip: get only the number of subsarrays with sum <= the actual goal
# then get the subarrays with sum <= goal - 1
# at the end to solve the problem substract from the first sum the second one to get 
# number of subarrays with sum == goal
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def slidingwindow(current_goal: int) -> int:
            l = 0
            curr_sum, total = 0, 0
            for r in range(len(nums)):
                curr_sum += nums[r]
                while l <= r and curr_sum > current_goal:
                    curr_sum -= nums[l]
                    l += 1
                total += r - l + 1 #size of subarray with sum <= current goal
            return total
        
        tot_goal = slidingwindow(goal) 
        tot_goal_minus_one = slidingwindow(goal - 1)
        return tot_goal - tot_goal_minus_one