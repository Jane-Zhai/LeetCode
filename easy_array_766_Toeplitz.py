class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
        给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
        """
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True


class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            if matrix[i][1:] != matrix[i-1][0:len(matrix[0])-1]:
                return False
        return True


sol = Solution()
print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
                    