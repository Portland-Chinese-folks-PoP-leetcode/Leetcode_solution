def rightbound(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            left = mid+1  # 所以其实是从这边逃出去的
            print('lastloop1')
        elif nums[mid] < target:
            left = mid+1
            print('lastloop2')
        elif nums[mid] > target:
            right = mid
            print('lastloop3')
    print('right position is ', right, left)
    if right == 0:
        return -1
    return (right-1) if nums[right-1] == target else -1


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
    print('right position is ', right)
    if right < 0 or nums[right] != target:
        return -1
    return right


nums = [1, 2, 3, 4, 5, 6]
print(rightbound(nums, 1))
