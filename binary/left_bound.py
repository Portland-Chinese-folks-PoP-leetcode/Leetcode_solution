def leftbound(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            # 为什么这边是right=mid 因为while的condition 是左闭右开的 [left,mid)所以不会渠道这个mid,
            right = mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    if left == len(nums):
        return -1
    return left if nums[left] == target else -1


def leftbound(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            right = mid-1
        elif nums[mid] > target:
            right = mid-1
        elif nums[mid] < target:
            left = mid+1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left
