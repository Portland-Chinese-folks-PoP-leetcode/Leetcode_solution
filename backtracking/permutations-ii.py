class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        nums = sorted(nums)
        used = [False for i in range(len(nums))]

        def backtrack(nums):
            print(track)
            if len(track) == len(nums):
                res.append(list(track))
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums)
                track.pop(-1)
                used[i] = False

        backtrack(nums)
        return res


# 为什么会有这种情况下不加入中间的1了呢？ 因为tm回不去了，操
a = Solution()
nums = [1, 1, 2]
a.permuteUnique(nums)
