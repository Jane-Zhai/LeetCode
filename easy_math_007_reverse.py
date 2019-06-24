class Solution:
    def reverse(self, x):
        """
        给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
        """
        n = x if x > 0 else -x
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n//10
        if res > 0x7ffffff:
            return 0 
        return res if x>0 else -res
        

sol = Solution()
print(sol.reverse(123))