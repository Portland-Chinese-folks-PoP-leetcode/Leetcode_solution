# Leetcode_solution

This is Yune's Leetcode repo. I build this repo to help cs and cs align students in northeastern university to better crack leetcode solution. Some of the code is still navie and perhaps not the best way. I still have a long path to walk ahead. But The repo implement a template idea. There are currently 80 more leetcode solution in the repo.

All the code here is according to [labuladong](https://github.com/labuladong/fucking-algorithm), but a python version. If you were a labuladong reader , but you prefer to use python as your weapon on leetcode. You are in the right battle field.

I build this repo initially in this [organization](https://github.com/Portland-Chinese-folks-PoP-leetcode/Leetcode_solution), If you want to check some template written in python. Go to [issue tab](https://github.com/Portland-Chinese-folks-PoP-leetcode/Leetcode_solution/issues) 

Rule No.1 
- Don't be a coward before algorithem problems. Show me your gut, and let's fuck algorithem.

![output](img/fight_club.png)

Rule No.2
- Talk is cheap, Code is valuable. So Shut The Fuck Up. 《话越多越菜》

![output](img/Pulp-Fiction.jpeg)

复习 第一轮()
# 复习的第一个周期（3天）
#### single linked list
- [merge-k-sorted-lists](https://leetcode.cn/problems/merge-k-sorted-lists/submissions/) [**solution**](linked_list/merge-k-sorted-lists-priorityqueue-version.py)
- [merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists/)  [**solution**](linked_list/merge-two-sorted-lists.py)
- [remove-nth-node-from-end-of-list](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/submissions/)  [**solution**](linked_list/remove-nth-node-from-end-of-list.py)  先后指针
- [middle-of-the-linked-list](https://leetcode.cn/problems/middle-of-the-linked-list/submissions/)  [**solution**](linked_list/middle-of-the-linked-list.py) 快慢指针
- [linked-list-cycle](https://leetcode.cn/problems/linked-list-cycle/submissions/)   [**solution**](linked_list/linked-list-cycle.py) 快慢指针
- [linked-list-cycle-ii](https://leetcode.cn/problems/linked-list-cycle-ii/submissions/)   [**solution**](linked_list/linked-list-cycle-ii.py) 第一次相遇 fast和 slow速度不同，相遇后slow退回head，跑到再次相遇（此时快慢速度一样）
- [intersection-of-two-linked-lists](https://leetcode.cn/problems/intersection-of-two-linked-lists/)   [**solution**](linked_list/intersection-of-two-linked-lists.py)


#### 反转 single linked list
- [reverse-linked-list](https://leetcode.cn/problems/reverse-linked-list/)  [**solution**](linked_list/reverse-linked-list.py)   递归实现反转单链表(模板)， 需要背熟
- [reverse-linked-list-ii](https://leetcode.cn/problems/reverse-linked-list-ii/)   [**solution**](linked_list/reverse-linked-list-ii.py)  python的实现不太一样 需要背熟
- [reverse-nodes-in-k-group](https://leetcode.cn/problems/reverse-nodes-in-k-group/submissions/)     [**solution**](linked_list/reverse-nodes-in-k-group.py)  用迭代实现反转

#### 回文串 |<—— left right ——>|
- [valid-palindrome](https://leetcode.cn/problems/valid-palindrome/submissions/)   [**solution**](string/valid-palindrome.py) 
- [palindrome-linked-list](https://leetcode.cn/problems/palindrome-linked-list/submissions/)   [**solution 1**](linked_list/palindrome-linked-list.py)   [**solution 2**](linked_list/palindrome-linked-list-v2.py) 

#### binary  |left——> <——right|
- [binary-search](https://leetcode.cn/problems/binary-search/)   [**solution**](binary/binary-search.py)
- [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)  [**solution**](binary/find-first-and-last-position-of-element-in-sorted-array-v2.py) 
- [search-insert-position](https://leetcode.cn/problems/search-insert-position/)   [**solution**](binary/search-insert-position.py) 

#### double pointer 双指针
- [remove-duplicates-from-sorted-array](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)    [**solution**](doublePointer/remove-duplicates-from-sorted-array.py)   原地修改数组 (快慢)
- [remove-duplicates-from-sorted-list](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/submissions/)   [**solution**](doublePointer/remove-duplicates-from-sorted-list.py) 原地修改链表 (快慢)
- [remove-element](https://leetcode.cn/problems/remove-element/)  [**solution**](doublePointer/remove-element.py) 原地修改数组 (快慢)
- [move-zeroes](https://leetcode.cn/problems/move-zeroes/)    [**solution**](doublePointer/moveZeroes.py) 原地修改数组 (快慢)
- [two-sum-ii-input-array-is-sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)   [**solution**](doublePointer/two-sum-ii-input-array-is-sorted.py) （两边向中间move的指针）
- [reverse-string](https://leetcode.cn/problems/reverse-string)    [**solution**](doublePointer/reverse-string.py)(两边向中间move的指针)
- [longest-palindromic-substring](https://leetcode.cn/problems/longest-palindromic-substring/)   [**solution**](doublePointer/longest-palindromic-substring.py)(中间向两边move的指针)    

#### slidng window(典型快慢指针，快慢中间就是所谓的窗口)，用于结局子串问题
- [minimum-window-substring](https://leetcode.cn/problems/minimum-window-substring)  [**solution**](slidingWindow/minimum-window-substring.py)
- [permutation-in-string](https://leetcode.cn/problems/permutation-in-string)  [**solution**](slidingWindow/permutation-in-string.py)
- [find-all-anagrams-in-a-string](https://leetcode.com/problems/find-all-anagrams-in-a-string/) [**solution**](slidingWindow/find-all-anagrams-in-a-string.py)
- [longest-substring-without-repeating-characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters) [**solution**](slidingWindow/longest-substring-without-repeating-characters.py)

#### Nsum
- [two-sum](https://leetcode.cn/problems/two-sum/)
- [two-sum-ii-input-array-is-sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)
- [3sum](https://leetcode.cn/problems/3sum/)
- [4sum](https://leetcode.cn/problems/4sum/)


#### 前缀
- [range-sum-query-immutable](https://leetcode.cn/problems/range-sum-query-immutable/)
- [range-sum-query-2d-immutable](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

#### 差分数组difference array
- [range-addition](https://leetcode.cn/problems/range-addition/submissions/)
- [corporate-flight-bookings](https://leetcode.cn/problems/corporate-flight-bookings/)
- [car-pooling](https://leetcode.cn/problems/car-pooling/submissions/)

#### section_name
- [question_name](leetcode_link)  [**Solution**](relative_path)