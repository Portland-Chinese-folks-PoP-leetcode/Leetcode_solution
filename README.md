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
# 复习的第一个周期（3天）实际用时4天
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

#### Nsum 这玩意就得背熟，尤其里面那个NsumTarget(nums,n,start,target)函数，是真的难打
- [two-sum](https://leetcode.cn/problems/two-sum/)   [**solution**](N-sum/two-sum.py)
- [two-sum-ii-input-array-is-sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)    [**solution**](doublePointer/two-sum-ii-input-array-is-sorted.py)
- [3sum](https://leetcode.cn/problems/3sum/)    [**solution**](N-sum/threeSum.py)
- [4sum](https://leetcode.cn/problems/4sum/)    [**solution**](N-sum/4sum.py)


#### 前缀和/积 rangeSum。 本质是用一个新数组preSum来存储元数组的累加和或者累加积，以使得算法的时间复杂度打到O(1),when we creating the presum array, the length of row or column is always 1 bigger than the original one 
- [range-sum-query-immutable](https://leetcode.cn/problems/range-sum-query-immutable/)    [**solution**](rangesum前缀/range-sum-query-immutable.py)
- [range-sum-query-2d-immutable](https://leetcode.cn/problems/range-sum-query-2d-immutable/)    [**solution**](rangesum前缀/range-sum-query-2d-immutable.py)

#### 差分数组difference array
- [range-addition](https://leetcode.cn/problems/range-addition/submissions/)    [**solution**](differenceArray/range-addition.py)
- [corporate-flight-bookings](https://leetcode.cn/problems/corporate-flight-bookings/)    [**solution**](differenceArray/corporate-flight-bookings.py)
- [car-pooling](https://leetcode.cn/problems/car-pooling/submissions/)    [**solution**](differenceArray/car-pooling.py)

# 复习的第二轮 (费城回来以后)


## 二叉树

#### [二叉树_基操篇](https://labuladong.github.io/algo/2/19/40/) 判断 BST 的合法性、增、删、查。其中「删」和「判断合法性」略微复杂
- [validate-binary-search-tree](https://leetcode.cn/problems/validate-binary-search-tree/)  [**Solution**](Binary_tree/二叉搜索树_基操篇/delete-node-in-a-bst.py)
- [delete-node-in-a-bst](https://leetcode.cn/problems/delete-node-in-a-bst/)  [**Solution**](Binary_tree/二叉搜索树_基操篇/delete-node-in-a-bst.py)
- [search-in-a-binary-search-tree](https://leetcode.cn/problems/search-in-a-binary-search-tree/)  [**Solution**](Binary_tree/二叉搜索树_基操篇/search-in-a-binary-search-tree.py)
- [insert-into-a-binary-search-tree](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)  [**Solution**](Binary_tree/二叉搜索树_基操篇/insert-into-a-binary-search-tree.py)


#### [二叉树_构造篇](https://labuladong.github.io/algo/2/19/41/) 
- [unique-binary-search-trees-ii](https://leetcode.cn/problems/unique-binary-search-trees-ii/)  [**Solution**](Binary_tree/二叉搜索树_构造篇/unique-binary-search-trees-II.py)
- [unique-binary-search-trees](https://leetcode.cn/problems/unique-binary-search-trees/)  [**Solution**](Binary_tree/二叉搜索树_构造篇/unique-binary-search-trees.py)

#### [二叉树_特性篇](https://labuladong.github.io/algo/2/19/39/) 
- [kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)  [**Solution**](Binary_tree/二叉树_特性_中序/kth-smallest-element-in-a-bst.py)
- [convert-bst-to-greater-tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)  [**Solution**](Binary_tree/二叉树_特性_中序/convert-bst-to-greater-tree.py)
- [binary-search-tree-to-greater-sum-tree](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/)  [**Solution**](relative_path) 这题我还没做

#### [二叉树_思路](https://labuladong.github.io/algo/2/19/34/) 
- [flatten-binary-tree-to-linked-list](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)  [**Solution**](Binary_tree/二叉树_思路/flatten-binary-tree-to-linked-list.py)
- [populating-next-right-pointers-in-each-node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)  [**Solution**](Binary_tree/二叉树_思路/populating-next-right-pointers-in-each-node.py)
- [invert-binary-tree](https://leetcode.cn/problems/invert-binary-tree/)  [**Solution**](Binary_tree/二叉树_思路/invert-binary-tree.py)

#### [二叉树_构造](https://labuladong.github.io/algo/2/19/35/) 
- [construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)  [**Solution**](Binary_tree/二叉树_构造/construct-binary-tree-from-preorder-and-inorder-traversal.py)
- [construct-binary-tree-from-inorder-and-postorder-traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)  [**Solution**](Binary_tree/二叉树_构造/construct-binary-tree-from-inorder-and-postorder-traversal.py)
- [maximum-binary-tree](https://leetcode.cn/problems/maximum-binary-tree/)  [**Solution**](Binary_tree/二叉树_构造/maximum-binary-tree.py)
- [construct-binary-tree-from-preorder-and-postorder-traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)  [**Solution**](Binary_tree/二叉树_构造/construct-binary-tree-from-preorder-and-postorder-traversal.py)

#### [二叉树_序列化](https://labuladong.github.io/algo/2/19/36/) 
- [serialize-and-deserialize-binary-tree](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)  [**Solution 1**](Binary_tree/二叉树_序列化/serialize-and-deserialize-binary-tree.py)  [**Solution 2**](Binary_tree/二叉树_序列化/BFS-serialize-and-deserialize-binary-tree.py)


#### [二叉树_后序](https://labuladong.github.io/algo/2/19/37/) 
- [find-duplicate-subtrees](https://leetcode.cn/problems/find-duplicate-subtrees/)  [**Solution**](Binary_tree/二叉树_后序/find-duplicate-subtrees.py)


#### [二叉树_纲领](https://labuladong.github.io/algo/2/19/33/) 


-[question_name](leetcode_link)  [**Solution**](relative_path)


-[question_name](leetcode_link)  [**Solution**](relative_path)
 

## 暴力穷举

#### backtracking回溯

[回溯算法解题套路框架](https://labuladong.github.io/algo/4/29/103/)
- [n-queens](https://leetcode.cn/problems/n-queens/)  [**Solution**](backtracking/n-queens.py)
- [permutations](https://leetcode.cn/problems/permutations/)  [**Solution**](backtracking/permutations.py) 用了printindent的操作(这个套路很骚，适用于所有递归)
  
[经典回溯算法：集合划分问题](https://labuladong.github.io/algo/4/29/104/)
- [partition-to-k-equal-sum-subsets](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)  [**Solution**](backtracking/partition-to-k-equal-sum-subsets.py)

[回溯算法秒杀所有排列/组合/子集问题](https://labuladong.github.io/algo/4/29/105/)

- [permutations](https://leetcode.cn/problems/permutations/)  [**Solution**](backtracking/permutations.py) 用了printindent的操作(这个套路很骚，适用于所有递归)
- [subsets](https://leetcode.cn/problems/subsets/)  [**Solution**](backtracking/subsets.py)
- [subsets-ii](https://leetcode.cn/problems/subsets-ii/)  [**Solution**](backtracking/subsets-ii.py)
- [permutations-ii](https://leetcode.cn/problems/permutations-ii/)  [**Solution**](backtracking/permutations-ii.py)
- [combinations](https://leetcode.cn/problems/combinations/)  [**Solution**](backtracking/combinations.py)
- [combination-sum](https://leetcode.cn/problems/combination-sum/)  [**Solution**](backtracking/combination-sum.py)
- [combination-sum-ii](https://leetcode.cn/problems/combination-sum-ii/)  [**Solution**](backtracking/combination-sum-ii.py)
- [combination-sum-iii](https://leetcode.cn/problems/combination-sum-iii)  [**Solution**](relative_path) 这题我还没做

[回溯算法最佳实践：括号生成](https://labuladong.github.io/algo/4/29/108/)
- [generate-parentheses](https://leetcode.cn.com/problems/generate-parentheses/submissions/)  [**Solution**](backtracking/generate-parentheses.py)



  
#### islands
- a simple framework demo for island  [**Solution**](islands/island_framework.py)
- [number-of-islands](https://leetcode.cn/problems/number-of-islands/)  [**Solution**](**islands/number-of-islands.py)
- [number-of-distinct-islands](https://leetcode.cn/problems/number-of-distinct-islands/)  [**Solution**](islands/number-of-distinct-islands.py)
- [max-area-of-island](https://leetcode.cn/problems/max-area-of-island/)  [**Solution**](islands/max-area-of-island.py)
- [number-of-enclaves](https://leetcode.cn/problems/number-of-enclaves/)  [**Solution**](islands/number-of-enclaves.py)
- [number-of-closed-islands](https://leetcode.cn/problems/number-of-closed-islands/)  [**Solution**](islands/number-of-closed-islands.py)
- [count-sub-islands](https://leetcode.cn/problems/count-sub-islands/)  [**Solution**](islands/count-sub-islands.py)




#### BFS

#### section_name
- [question_name](leetcode_link)  [**Solution**](relative_path)


## DP

#### 一维
#### 二维
#### memorization