class Solution(object):
    def hasAlternatingBits(self, n):
        """
        给定一个正整数，检查他是否为交替位二进制数：
        换句话说，就是他的二进制数相邻的两个位数永不相等。
        :type n: int
        :rtype: bool
        """
        t = n ^ (n>>1)
        return (t&(t+1))==0

class Solution2(object):
    def hasAlternatingBits(self, n):
        return not ('11' in str(bin(n)) or '00' in str(bin(n)))

sol = Solution()
print(sol.hasAlternatingBits(5)) 
