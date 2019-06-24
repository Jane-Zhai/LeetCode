class Solution(object):
    def findComplement(self, num):
        """
        给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
        注意:
        给定的整数保证在32位带符号整数的范围内。
        你可以假定二进制数不包含前导零位。
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1
        return (i-1) ^ num


sol = Solution()
print(sol.findComplement(5)) 