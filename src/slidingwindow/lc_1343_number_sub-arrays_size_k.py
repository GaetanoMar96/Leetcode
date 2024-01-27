class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        currsum = 0
        curravg = 0
        size = 0
        for r in range(len(arr)):
            currsum += arr[r]
            size += 1
            while size == k: #shrink the window
                curravg = currsum // k
                if curravg >= threshold:
                    res += 1
                currsum -= arr[l]
                size -= 1
                l += 1

        return res