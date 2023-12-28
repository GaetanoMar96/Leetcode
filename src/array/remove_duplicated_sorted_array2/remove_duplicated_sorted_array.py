"""

"""

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        pt1 = 0
        pt2 = 1
        size = len(nums)
        count = 1
        k = 0
        while pt2 < size:
            num1 = nums[pt1]
            num2 = nums[pt2]
            if num1 == num2 and count == 2:
                nums.remove(num1)
                size -= 1
                continue
            elif num1 == num2 and count < 2:
                count += 1
            elif num1 != num2:
                count = 1
            pt1 += 1
            pt2 += 1

        return size 