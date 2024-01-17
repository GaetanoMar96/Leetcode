class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        def bs(l, h):
            while l <= h:
                m = (l+h) // 2
                if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                    return m
                if arr[m] > arr[m+1]:
                    h = m
                else:
                    l = m + 1
            return l
        return bs(0, len(arr)-1)