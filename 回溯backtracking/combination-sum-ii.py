# https://leetcode-cn.com/problems/combination-sum-ii/submissions/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        candidates = sorted(candidates)
        tracksum = 0

        def backtrack(candidates, start, tracksum):
            if tracksum == target and track not in res:
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
