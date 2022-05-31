
def subsetsWithDup(nums):
    track = []
    res = []
    nums = sorted(nums)

    def backtrack(nums, start):
        res.append(list(track))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            track.append(nums[i])
            backtrack(nums, i+1)
            track.pop(-1)
    backtrack(nums, 0)
    return res


# following code is just for fun
"""In the following example, the greet function takes 
another function as a parameter(subsetsWithDup in this case). 
The function passed as an argument is then called inside the function play.
"""
def play(subsetsWithDup):
    nums = [1, 2, 2, 3]
    print(subsetsWithDup(nums))


play(subsetsWithDup)

# 排序和剪枝的逻辑。
# 体现在代码上，需要先进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过：
