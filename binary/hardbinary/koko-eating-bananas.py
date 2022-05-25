class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(piles, x):
            hours = 0
            for i in range(len(piles)):
                hours += piles[i] // x
                if piles[i] % x > 0:
                    hours += 1
            return hours

        left = 1
        right = sum(piles)-1
        while left <= right:
            mid = left+(right-left)//2
            if f(piles, mid) == h:
                right = mid-1
            elif f(piles, mid) < h:
                right = mid-1
            elif f(piles, mid) > h:
                left = mid+1
        print(left)
        # if left>=1000000000 or f(piles,left)>h: return -1
        return left
