class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        """
        给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。
        操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。
        在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
        """
        # 每次操作都是左上角区域从（0, 0）到（a, b）的矩形，
        # 必定重叠，所以找最小的a乘最小的b就行
        if not ops:
            return m*n
        m = ops[0][0]
        n = ops[0][1]
        for a in ops[1:]:
            m = min(m,a[0])
            n = min(n,a[1])
        return m * n


sol = Solution()
print(sol.maxCount(3,3,[[2,2],[3,3]]))