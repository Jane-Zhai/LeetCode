class Solution(object):
    def getSum(self, a, b):
        """
        不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
        :type a: int
        :type b: int
        :rtype: int
        """
        sum = a ^ b
        carry = (a & b) << 1
        if carry != 0:
            sum += carry
        return sum

class Solution2(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        """有疑问,python把有符号数当作无符号数处理"""
        return a if a <= MAX else ~(a ^ mask)
        
sol = Solution()
print(sol.getSum(2,-2))