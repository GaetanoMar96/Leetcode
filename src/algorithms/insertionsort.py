def insertionSort(nums: list[int]):
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key 