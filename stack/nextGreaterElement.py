def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement_for_nums2(nums: List[int]):
        n = len(nums)
        res = [None]*n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i]:
                aaa = stack.pop()
            res[i] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[i])
        return res
