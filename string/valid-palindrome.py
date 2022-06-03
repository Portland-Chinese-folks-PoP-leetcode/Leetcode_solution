class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = list(s)
        newstring = ''
        for i in string_list:
            if i.isnumeric() or i.isalpha():
                newstring = newstring+i.lower()

        string_list = list(newstring)
        left = 0
        right = len(string_list)-1

        if len(string_list) == 1:
            return True
        while left < right:
            if string_list[left] != string_list[right]:
                return False
            left += 1
            right -= 1
        return True
# 第二次刷这个题所使用的方法 new_string=''.join(ch.lower() for ch in s if ch.isalnum()) 这一步很有意思，


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(new_string)-1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
        return True
