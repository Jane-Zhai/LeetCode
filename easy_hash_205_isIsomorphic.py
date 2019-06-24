class Solution:
    def isIsomorphic(self, s, t):
        """
        给定两个字符串 s 和 t，判断它们是否是同构的。
        如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
        所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
        """
        if len(s) != len(t):
            return False
        sdic = dict()
        tdic = dict()
        for i in range(len(s)):
            if (s[i] in sdic and sdic[s[i]] != t[i])\
                or (t[i] in tdic and tdic[t[i]] != s[i]):
                return False
            else:
                sdic[s[i]] = t[i]
                tdic[t[i]] = s[i]
        return True


class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

        
sol = Solution()
print(sol.isIsomorphic("foo","adr"))
