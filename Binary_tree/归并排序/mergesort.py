class Solution(object):
    temp = []

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        This is the best descriptio for merge I have seen ever
        The merge Function:

This function merges two sorted halves of the nums array.
Arguments: nums (the list to be sorted), low (starting index of the left half), mid (ending index of the left half), and high (ending index of the right half).
A temporary array temp is used to store the elements of nums between low and high.
The merging process uses two pointers, i and j. i starts from the beginning of the left half and j from the beginning of the right half.
As the merging progresses, the smaller of the two values pointed to by i and j is added to the sorted nums and the respective pointer is incremented.
        """
        def merge(nums, low, mid, high):
            print(nums, low, high)
            for i in range(low, high+1):
                temp[i] = nums[i]
            i = low
            j = mid+1
            for p in range(low, high+1):
                if i == mid+1:
                    # 左半边数组已全部被合并
                    nums[p] = temp[j]
                    j += 1
                elif j == high+1:
                    # 右半边数组已全部被合并
                    nums[p] = temp[i]
                    i += 1
                elif temp[i] > temp[j]:
                    nums[p] = temp[j]
                    j = j+1
                else:
                    nums[p] = temp[i]
                    i += 1

        def mergesort(nums, low, high):
            if low == high:
                return
            mid = low+(high-low)//2
            mergesort(nums, low, mid)
            mergesort(nums, mid+1, high)
            merge(nums, low, mid, high)
        temp = [None for i in range(len(nums))]
        mergesort(nums, 0, len(nums)-1)
        return nums


nums = [5, 2, 3, 1]
a = Solution()
print(a.sortArray(nums))
