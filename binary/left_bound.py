def leftbound(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    return left
