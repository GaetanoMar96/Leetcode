def selectionSort(nums: list[int]):
    for i in range(len(nums) - 1):
        currmin = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[currmin]:
                currmin = j
        nums[i], nums[currmin] = nums[currmin], nums[i]
