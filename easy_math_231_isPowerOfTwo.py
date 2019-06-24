class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

        2的幂次方在二进制下，只有1位是1，其余全是0。
        例如:8---00001000。负数的在计算机中二进制表示为补码(原码->正常二进制表示，原码按位取反(0-1,1-0)，最后再+1。
        然后两者进行与操作，得到的肯定是原码中最后一个二进制的1。
        例如8&(-8)->00001000 & 11111000 得 00001000，即8。
        """
        return n>0 and (n & -n)==n

class Solution2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        考虑二进制的解法，对于2的倍数来说，它只有一位二进制位不为0，
        而相邻两个数的按位与有一个特点，就是把大数的最低一位1变为0，
        举个例子：3的二进制是 11，2的二进制是10，二者按位与是10，3的最后一位1变为了0
        """
        return n>0 and not (n & n-1)


sol = Solution()
print(sol.isPowerOfTwo(12))