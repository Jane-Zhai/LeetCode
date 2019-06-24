class Solution:
    def isPalindrome(self, x):
        """
        判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
        """
        if x < 0:
            return False
        
        n = 1
        while x/n>=10:
            n *= 10
        
        while x:
            
            head = x // n
            tail = x % 10

            if head != tail:
                return False

            x= x % n
            x=x//10
            n/=100
        return True


sol = Solution()
print(sol.isPalindrome(31213))