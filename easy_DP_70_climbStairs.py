class Solution(object):
    def climbStairs(self, n):
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(2,n+1):
            a,b = b,a+b
        return b


from functools import lru_cache
class Solution2:
    @lru_cache(10**8)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution3(object):
    def climbStairs(self, n):
        if n<1:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        
        memo = dict()
        if n in memo:
            return memo[n]
        else:
            value = self.climbStairs(n-1)+self.climbStairs(n-2)
            memo.get(n,value)
            return value

        

sol = Solution3()
print(sol.climbStairs(5)) 
