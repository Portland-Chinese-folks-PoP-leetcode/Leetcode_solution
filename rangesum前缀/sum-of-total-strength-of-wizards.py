from itertools import accumulate


def totalStrength(A):
    mod = 10 ** 9 + 7
    n = len(A)

    # next small on the right
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and A[stack[-1]] > A[i]:
            right[stack.pop()] = i
        stack.append(i)
    print(right)
    # next small on the left
    left = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            left[stack.pop()] = i
        stack.append(i)
    print(left)
    # for each A[i] as minimum, calculate sum
    res = 0
    acc = list(accumulate(accumulate(A), initial=0))
    print(acc)
    for i in range(n):
        l, r = left[i], right[i]
        lacc = acc[i] - acc[max(l, 0)]
        racc = acc[r] - acc[i]
        ln, rn = i - l, r - i
        res += A[i] * (racc * ln - lacc * rn)
    return res


testcase1 = [1, 3, 1, 2]
totalStrength(testcase1)
