class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start):
            # print('track is ',self.track)
            # print('res is ',self.res)
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop(-1)
        res = []
        track = []
        backtrack(nums, 0)
        return res
