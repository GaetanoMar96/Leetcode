class Solution:
    #First approach modifying array, Time complexity O(nlogn), Space complexity O(1)
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        pt1 = 0
        pt2 = 1
        size = len(nums)
        while pt2 <= size:
            num1 = nums[pt1]
            num2 = nums[pt2]
            if num1 == num2:
                return num1
            if pt2 == size - 1:
                break
            pt1 += 1
            pt2 += 1
        return -1

    #Second approach using floyd detect cycle, Time complexity O(n), Space complexity O(1)
    def findDuplicateOptimized(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
