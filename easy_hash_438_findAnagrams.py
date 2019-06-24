class Solution:
    def findAnagrams(self, s, p):
        """
        给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
        字母异位词指字母相同，但排列不同的字符串。
        不考虑答案输出的顺序。
        """
        res = []
        left = right = 0
        count = len(p)
        dic = dict()
        for i in p:
            dic[i] = dic.get(i,0)+1
        while right < len(s):
            if s[right] in dic.keys():
                if dic[s[right]]>=1:
                    count = count - 1
                dic[s[right]] = dic[s[right]]-1
            right = right+1
            if count == 0 :
                res.append(left)
            if right - left == len(p):
                if s[left] in dic.keys():
                    if dic[s[left]]>=0:
                        count = count + 1
                    dic[s[left]]+=1
                left = left+1
        return res


sol = Solution()
print(sol.findAnagrams("cbaebabacd","abc"))