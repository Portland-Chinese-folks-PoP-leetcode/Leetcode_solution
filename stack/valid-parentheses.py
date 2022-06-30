# https://leetcode.cn/problems/valid-parentheses/
# labuladong解法用 list实现
class Solution:
    def isValid(self, s: str) -> bool:
        def leftof(c):
            if c == ')':
                return '('
            if c == '}':
                return '{'
            if c == ']':
                return '['
        # When encounter left paranthesis push the left parentehsis into the stack,else find the most close right parenthesis
        left_stack = []
        for c in list(s):
            if c == '(' or c == '{' or c == '[':
                left_stack.append(c)
            else:
                print(left_stack)
                if len(left_stack) > 0 and left_stack[-1] == leftof(c):
                    left_stack.pop(-1)
                else:
                    return False
        return True if len(left_stack) == 0 else False


s = Solution()
test_string = '[]'
s.isValid(test_string)
