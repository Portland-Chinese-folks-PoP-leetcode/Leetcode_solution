# https: // leetcode.cn/problems/combination-sum-iii/
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, 10)]
        track = []
        res = []

        def backtrack(nums, start, tracksum):
            if tracksum == n and len(track) == k:
                res.append(list(track))
            if tracksum > n or len(track) > k:
                return
            for i in range(start, len(nums)):
                # 做选择
                tracksum += nums[i]
                track.append(nums[i])
                # 注意参数
                backtrack(nums, i+1, tracksum)
                # 撤销选择
                tracksum -= nums[i]
                track.pop(-1)
        backtrack(nums, 0, 0)
        return res
