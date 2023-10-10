# https://leetcode.cn/problems/permutation-in-string/submissions/
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {i: 0 for i in s1}
        window = {i: 0 for i in s2}
        for c in s1:
            need[c] += 1
        left, right, valid = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right-left >= len(s1):
                #在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
    
    ## 下面这个办法明显更好更直观
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the length of s1 and s2
        len_s1, len_s2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s1 to be a permutation of a substring of s2
        if len_s1 > len_s2:
            return False
        
        # Get the frequency count of characters in s1
        count_s1 = Counter(s1)
        print("count_s1 is ", count_s1)
        # Get the frequency count of the first window in s2
        window_count = Counter(s2[:len_s1])
        print(window_count)
        # Check if the first window in s2 is a permutation of s1
        if count_s1 == window_count:
            return True
        
        # Slide the window through s2
        for i in range(len_s1, len_s2):
            # Update the window count
            window_count[s2[i]] += 1  # Add the new character
            window_count[s2[i-len_s1]] -= 1  # Remove the first character of the previous window
            
            # Remove the count of the character if it becomes 0
            if window_count[s2[i-len_s1]] == 0:
                del window_count[s2[i-len_s1]]
            
            # Check if the current window is a permutation of s1
            if count_s1 == window_count:
                return True
        
        # If no window is a permutation of s1, return False
        return False
