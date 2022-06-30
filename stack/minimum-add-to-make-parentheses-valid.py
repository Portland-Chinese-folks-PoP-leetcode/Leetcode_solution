# https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        num_valid = 0

        def leftof(c):
            if c == ')':
                return '('
            if c == ']':
                return '[]'
            if c == '}':
                return '{}'
        for c in list(s):
            if c == '(' or c == '(' or c == '(':
                stack.append(c)
            else:
                if len(stack) > 0 and leftof(c) == stack[-1]:
                    stack.pop(-1)
                    num_valid += 1
        res = len(s)-num_valid*2
        return res
