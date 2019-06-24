class Solution:
    def longestPalindrome(self, s):
        """
        给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
        在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
        """
        length = 0
        odd = 0
        dic = dict()

        for i in s:
            dic[i]=dic.get(i,0)+1
        for i in dic:
            if dic[i]%2==0:
                length += dic[i]
            else:
                odd = 1
        return length+odd


class Solution2:
    def longestPalindrome(self, s):
        return len(s) - max(0,sum([s.count(i)%2 for i in set(s)])-1)


sol = Solution2()
print(sol.longestPalindrome("ccccdd"))


