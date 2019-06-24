class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        给定一个正整数 num，编写一个函数，
        如果 num 是一个完全平方数，则返回 True，否则返回 False。
        """
        r = num
        while r*r>num:
            r = (r+num/r)//2
        return r*r==num

class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        """
        利用 1+3+5+7+9+…+(2n-1)=n^2，即完全平方数肯定是前n个连续奇数的和
        """
        sum = 1
        while num>0:
            num-=sum
            sum+=2
        if num == 0:
            return True
        else:
            return False


sol = Solution2()
print(sol.isPerfectSquare(27))