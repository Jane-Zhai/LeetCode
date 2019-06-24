class Solution:
    def firstUniqChar(self, s):
        """
        给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
        """
        for i in s:
            if s.count(i)<2:
                return s.index(i)
        return -1


sol = Solution()
print(sol.firstUniqChar("loveleetcode"))