class Solution:
    def addBinary(self, a, b):
        """
        给定两个二进制字符串，返回他们的和（用二进制表示）。
        输入为非空字符串且只包含数字 1 和 0。
        """
        if a == '':
            print(a,b)
            return b
        if b == '':
            print(a,b)
            return a
        if a[-1] == '1' and b[-1] == '1':
            print(a,b)
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'
        elif a[-1] == '0' and b[-1] == '0':
            print(a,b)
            return self.addBinary(a[:-1],b[:-1]) + '0'
        else:
            print(a,b)
            return self.addBinary(a[:-1],b[:-1]) + '1'
            


sol = Solution()
print(sol.addBinary("1010","1011"))