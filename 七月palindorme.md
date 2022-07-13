# pay attention to subsequence and substring
- [longest-palindromic-subsequence](https://leetcode.cn/problems/longest-palindromic-subsequence/) [**Solution**](DP/longest-palindromic-subsequence.py) 这个是subset 区别这个和subsequence
dp 数组的定义是 dp[i][j]=x的定义是，string[i:j]内的最长回文子序列的长度。 二维dp
所以这个题目迭代的时候要从最后开始迭代，j却要从 range(i+1，n)内迭代。
if the length of string is 7, the last index of the string is 6
Then the sequence of (i,j) will be 
5,6
4,5
4,6
3,4
-[word-break](https://leetcode.cn/problems/word-break/) [**Solution**](DP/word-break.py) 
一维dp数组，返回值是true or false

-[word-break-ii](https://leetcode.cn/problems/word-break-ii/) [**Solution**](backtracking/word-break-ii.py)
这个用的是回溯 def backtrack(start,track), 选择列表是 word list

-[palindrome-number](https://leetcode.cn/problems/palindrome-number/) [**Solution**](backtracking/word-break-ii.py) 这是左右指针的问题 不过这个可以用来当判断一个序列是否是 回文串 palindrome 。It ask you if a number is a palindrome number
- [palindromic-substrings](https://leetcode.cn/problems/palindromic-substrings/) [**Solution**](DP/palindromic-substrings.py) Given a string s, return the number of palindromic substrings in it.
同样是利用这个dp数组
```
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        dp[i][j]=(s[i]==s[j]) and dp[i+1][j-1]
```
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```
- [longest-palindrome](https://leetcode.cn/problems/longest-palindrome/) [**Solution**](backtracking/longest-palindrome.py)
  ultilized counter from collections ,最后是用数学的方式在处理的这个问题 
- [palindrome-partitioning](https://leetcode.cn/problems/palindrome-partitioning/) [**Solution**](backtracking/palindrome-partitioning.py)
```Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```
utilize the dp[i][j] palindrome first then backtracking, for j in range(start,n), determine if dp[start][j] is a palindrome
- [longest-palindromic-substring](https://leetcode.cn/problems/longest-palindromic-substring/submissions/) [**Solution**](doublePointer/longest-palindromic-substring.py)
同样 利用 
```
for i in  range(n-1,-1,-1):
  for j in range(i+1,n):
    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

```