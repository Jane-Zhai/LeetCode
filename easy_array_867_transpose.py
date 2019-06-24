class Solution:
    def transpose(self, A):
        """"
        给定一个矩阵 A， 返回 A 的转置矩阵。
        """
        AT = list()
        ATcol = list()
        for col in range(len(A[0])):
            for row in A:
                ATcol.append(row[col])
            AT.append(ATcol)
            ATcol = []
        return AT


sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6]]))