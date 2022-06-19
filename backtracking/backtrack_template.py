# 无duplicates（distinct or unique 不可复选

# combination/subset
def backtrack(nums, start):
    for i in range(start, len(nums)):
        # 做选择
        track.append(nums[i])
        # 注意参数
        backtrack(nums, i+1)
        # 撤销选择
        track.pop(-1)

# permutation


def backtrack(nums, used):
    for i in range(len(nums)):
        # 剪枝逻辑
        if used[i] == True:
            continue
        # 做选择
        track.append(nums[i])
        used[i] = True
        backtrack(nums, used)
        # 撤销选择
        track.pop(-1)
        used[i] = False

# nums元素有重复不可复选

# combination/subset


nums = sorted(nums)


def backtrack(start, nums):
    for i in range(start, nums):
        if nums[i-1] == nums[i] and i > start:
            continue
        track.append(nums[i])
        backtrack(start+1, nums)
        track.pop(-1)


# permutation
nums = sorted(nums)


def backtrack(used, nums):
    for i in range(0, len(nums)):
        if used[i] == True:
            continue
        if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
            continue
        track.append(nums[i])
        used[i] = True
        backtrack(nums)
        track.pop(-1)
        used[i] = False

# 无重可复选


def backtrack(nums, start):
    for i in range(0, len(nums)):
        track.append(i)
        backtrack(nums, i)
        track.pop(-1)
