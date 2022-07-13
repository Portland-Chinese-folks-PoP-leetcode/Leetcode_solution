class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = list(str(x))
        print(reverse_x)
        left = 0
        right = len(reverse_x)-1
        while left <= right:
            if reverse_x[left] != reverse_x[right]:
                return False
            left += 1
            right -= 1
        return True
