# 这一题 while用<=, right=len(nums)-1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftbound(nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] < target:
                    left = mid+1
                if nums[mid] > target:
                    right = mid-1
                if nums[mid] == target:
                    right = mid-1
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def rightbound(nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] < target:
                    left = mid+1
                if nums[mid] > target:
                    right = mid-1
                if nums[mid] == target:
                    left = mid+1
                print()
            if right < 0 or nums[right] != target:
                return -1
            return right
        # #left=leftbound(nums,target)
        # right=rightbound(nums,target)
        # #print(left)
        # print(right)
        return[leftbound(nums, target), rightbound(nums, target)]
