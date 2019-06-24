import operator
from functools import reduce

class Solution:
    def findTheDifference(self, s, t):
        """"
        给定两个字符串 s 和 t，它们只包含小写字母。
        字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
        请找出在 t 中被添加的字母。
        """
        ss = sorted(s)
        tt = sorted(t)
        for i in range(len(ss)):
            if ss[i]!=tt[i]:
                return tt[i]
        return -1


class Solution2:
    def findTheDifference(self, s, t):        
        return chr(reduce(operator.xor, map(ord, (s + t))))
        

class Solution3(object):
    def findTheDifference(self, s, t):
        """
        异或
        """
        res = 0
        for i in s+t:
            res ^= ord(i)
        return chr(res)


sol = Solution3()
print(sol.findTheDifference("abcd","abcda"))