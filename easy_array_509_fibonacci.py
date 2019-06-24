class Solution:
    def fib(self, N):
        """
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
        Given N, calculate F(N).
        斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。
        给定 N，计算 F(N)。
        """

        if N == 0:
            return 0

        a = 0
        b = 1
        i = 0
        while i<N:
            a, b = b, a+b
            i += 1
        return a


class Solution2:
    def fib(self, N):
        if N < 2:
            return N
        return (self.fib(N-1) + self.fib(N-2))


sol = Solution2()
print(sol.fib(4)) 