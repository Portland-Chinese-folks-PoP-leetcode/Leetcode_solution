# https://leetcode-cn.com/problems/combination-sum-ii/submissions/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        candidates = sorted(candidates)
        tracksum = 0

        def backtrack(candidates, start, tracksum):
            if tracksum == target and track not in res:  # 其实在这种情况下 根本不需要在判断track 是否已经在res中因为经过剪枝的回溯树 根本不可能存在重复情况
                res.append(list(track))
            if tracksum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                tracksum = tracksum+candidates[i]
                track.append(candidates[i])
                backtrack(candidates, i+1, tracksum)
                track.pop(-1)
                tracksum = tracksum-candidates[i]
        backtrack(candidates, 0, tracksum)
        return res
    # 今天悟到另一个很重要的东西，continue 用于跳出循环的时候 ，单个return 用于跳出递归
    # 本题目 每个element 只能使用一次（can be only use once)
# 这种combination sum的回溯，利用了一个特性，词实了剪枝，一定要去先排序这个数组。然后在for循环中的每个element是不和他之前的elemet比较的，之后他后面的相加判断是否可以组成需要的target
