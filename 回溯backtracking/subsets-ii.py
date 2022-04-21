class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
