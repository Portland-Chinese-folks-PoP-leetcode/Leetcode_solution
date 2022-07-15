# https://leetcode.cn/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dic = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in str_dic:
                str_dic[key].append(string)
            else:
                str_dic[key] = [string]
        return list(str_dic.values())
