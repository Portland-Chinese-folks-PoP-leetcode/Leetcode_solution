class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def f(weights, x):
            days = 0
            cap = x
            i = 0
            while i < len(weights):
                cap = x
                while i < len(weights):
                    if cap < weights[i]:
                        break
                    else:
                        cap -= weights[i]
                    i += 1
                days += 1
            return days
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left+(right-left)//2
            if f(weights, mid) == days:
                right = mid-1
            elif f(weights, mid) < days:
                right = mid-1
            elif f(weights, mid) > days:
                left = mid+1
        return left
