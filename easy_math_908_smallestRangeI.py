class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        """
        给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
        在此过程之后，我们得到一些数组 B。
        返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
        """
        diff = max(A) - min(A)
        if K*2<=diff:
            res = diff - 2*K
        else:
            res = 0
        return res


sol = Solution()
print(sol.smallestRangeI([1,3,6],3))
