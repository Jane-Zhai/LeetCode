class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        给定一个整数 n，返回 n! 结果尾数中零的数量。
        你算法的时间复杂度应为 O(log n) 。
        """
        zerocnt = 0
        while n > 0:
            n //= 5
            zerocnt += n
        return zerocnt


sol = Solution()
print(sol.trailingZeroes(10))