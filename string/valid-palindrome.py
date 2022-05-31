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
