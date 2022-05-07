class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftbound(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid

            return left

        def rightbound(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    left = mid+1
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid
            return right-1
        if len(nums) == 0:
            return [-1, -1]
        elif target not in nums:
            return [-1, -1]

        return [leftbound(nums, target), rightbound(nums, target)]
