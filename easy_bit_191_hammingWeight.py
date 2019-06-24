class Solution(object):
    def hammingWeight(self, n):
        """
        编写一个函数，输入是一个无符号整数，
        返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
        :type n: int
        :rtype: int
        """
        # 直接判断二进制最低为的数是不是1
        count = 0
        while n:
            count += n&1
            n >>= 1
            
        return count

class Solution1(object):
    def hammingWeight(self, n):
        """
        除K取余法
        """
        ans=0
        while n:
            ans+=n%2
            n>>=1
        return ans


class Solution2(object):
    def hammingWeight(self, n):
        # 一个数与比自己小1的数按位与运算，
        # 会将自己所对应的二进制数的最后一个1变为0
        count = 0
        while n:
            n = n & (n-1)
            count = count + 1
        return count

sol = Solution()
print(sol.hammingWeight(32))

        