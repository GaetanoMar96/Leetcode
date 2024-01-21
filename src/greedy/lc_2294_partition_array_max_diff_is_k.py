class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        part = 0
        last = []
        for n in nums:
            if not last:
                last.append(n)
            else:
                if n - last[0] > k:
                    last = [n]
                    part += 1
        return part + 1