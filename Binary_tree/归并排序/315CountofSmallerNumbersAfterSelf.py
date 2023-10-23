def countSmaller(nums):
    def merge_sort(enums):
        mid = len(enums) // 2
        if mid:
            left, right = merge_sort(enums[:mid]), merge_sort(enums[mid:])
            for i in range(len(enums) - 1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                else:
                    enums[i] = right.pop()
        return enums

    smaller = [0] * len(nums)
    merge_sort(list(enumerate(nums)))
    return smaller


nums = [5,2,6,1]
print(countSmaller(nums)) ## [2, 1, 1, 0]
