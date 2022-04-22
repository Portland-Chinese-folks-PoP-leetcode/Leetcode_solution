class Solution:
    count = 0

    def printIndent(self, n):
        print("    "*n, end=' ')

    def permute(self, nums):

        def backtrack(nums, track, used):
            # self.count = self.count+1
            # self.printIndent(self.count)
            if len(track) == len(nums):
                # print('current track is ',track)
                """这一题的点睛之笔在这边
                因为这个 track 是一个外部引用，在遍历过程中track 中的数据会不断变化，
                所以装入 res 的时候应该把 track 里面的值做一次拷贝。Java 可以这样用 
                new 实现拷贝的效果，其他语言各有自己的方式。
                """
                res.append(list(track))
                # self.printIndent(self.count)
                # self.count = self.count-1
                # print(track)
                return
            for i in nums:
                if used[i] == True:
                    continue
                track.append(i)
                used[i] = True
                backtrack(nums, track, used)
                track.pop(-1)
                used[i] = False
        res = []
        track = []
        used = {i: False for i in nums}
        backtrack(nums, track, used)
        return res


solution = Solution()
nums = [1, 2, 3]
solution.permute(nums)
