def quickSort(nums: list[int]) -> list[int]:
    if not nums or len(nums) == 1:
        return nums

    pivot = nums[0]
    middlearray = []
    leftarray, rightarray = [], []
    for num in nums:
        if num < pivot:
            leftarray.append(num)
        elif num > pivot:
            rightarray.append(num)
        else:
            middlearray.append(num)
    
    return quickSort(leftarray) + middlearray + quickSort(rightarray)