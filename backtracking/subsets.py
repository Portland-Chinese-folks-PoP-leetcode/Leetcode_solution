from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start):
            # print('track is ',self.track)
            # print('res is ',self.res)
            res.append(list(track))
            print(track)
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop(-1)
        res = []
        track = []
        backtrack(nums, 0)
        return res


# https://leetcode-cn.com/problems/subsets/
nums = [1, 2, 3]
solution = Solution()
solution.subsets(nums)
