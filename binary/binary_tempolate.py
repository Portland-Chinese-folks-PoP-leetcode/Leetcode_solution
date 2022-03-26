class Solution:
    def search(self, nums: List, target: int) :
        l, r = 0, len(nums) - 1 
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        if nums[l] == target:
            return r
        return -1
    
    def search_2(self, nums: List[int], target: int):
        l, r = 0, len(nums) - 1 
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            return r
        return -1