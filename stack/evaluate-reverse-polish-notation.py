from typing import List
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(num1, num2, operator):

            if operator == '+':
                return int(num1) + int(num2)
            if operator == '-':
                return int(num1) - int(num2)
            if operator == '*':
                return int(num1) * int(num2)
            if operator == '/':
                return int(int(num1) / int(num2))
        stack = []
        for c in tokens:
            if c[-1].isnumeric():
                stack.append(c)
            else:
                a = stack.pop(-1)
                b = stack.pop(-1)
                intermedian = operate(b, a, c)
                stack.append(intermedian)
        return stack[0]


arr = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
for i in range(len(arr)):
    if arr[i][-1].isnumeric():
        arr[i] = int(arr[i])
print(arr)
