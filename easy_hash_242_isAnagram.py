class Solution:
    def isAnagram(self, s, t):
        """
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
        """
        if len(s)!=len(t):
            return False
        ss = sorted(list(s))
        tt = sorted(list(t))
        for i in range(len(ss)):
            if ss[i] != tt[i]:
                return False
        return True


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i,0)+1
        for i in t:
            dic2[i] = dic2.get(i,0)+1
        return dic1 == dic2


sol = Solution2()
print(sol.isAnagram("ana","nag"))