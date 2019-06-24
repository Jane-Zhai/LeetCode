class Solution:
    def sortedSquares(self, A):
        """"
        给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
        """
        for i in range(len(A)):
            A[i] **= 2
        A.sort()
        return A


sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))