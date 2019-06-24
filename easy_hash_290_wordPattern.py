class Solution:
    def wordPattern(self, pattern, str):
        """
        给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
        """
        dic1 = dict()
        dic2 = dict()
        string = str.split()
        for i,p in enumerate(pattern):
            # if p not in dic:
            #     dic[p]=string[i]
            # else:
            #     if dic[p]!=string[i]:
            #         return False
            if (p in dic1 and dic1[p]!=string[i])\
                or (string[i] in dic2 and dic2[string[i]]!=p):
                return False
            else:
                dic1[p]=string[i]
                dic2[string[i]]=p
        return True


class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        return len(pattern) == len(str.split(' ')) and \
            len(set(zip(pattern, str.split(' ')))) == \
            len(set(pattern)) == len(set(str.split(' ')))

sol = Solution()
print(sol.wordPattern("abba","cat dat dat cat"))