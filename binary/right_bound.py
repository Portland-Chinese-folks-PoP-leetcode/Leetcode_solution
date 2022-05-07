def rightbound(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    if left == 0:
        return -1
    return (left-1) if nums[left-1] == target else -1


def rightbound_v2(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
    if right < 0 or nums[right] != target:
        return -1
    return right
