def mergeSort(l:int, r: int, nums: list[int]) -> None:
    if l < r:
        mid = (l+r) // 2
        mergeSort(l, mid, nums)
        mergeSort(mid+1, r, nums)
        merge(l, mid, r, nums)

def merge(l:int, mid: int, r: int, nums: list[int]):
    array = []
    i = l
    j = mid + 1
    while i <= mid and j <= r:
        if nums[i] < nums[j]:
            array.append(nums[i])
            i += 1
        else:
            array.append(nums[j])
            j += 1
    while i <= mid:
        array.append(nums[i])
        i += 1
    while j <= r:
        array.append(nums[j])
        j += 1
    
    for k in range(l, r+1):
        nums[k] = array[k-l]