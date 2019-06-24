# class Solution:
#     def numMagicSquaresInside(self, grid):
#         """
#         3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
#         给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
#         """
#         # 找到3*3矩阵A...
#         # 判断A矩阵是不是
#             # 相等
#             # 不重复
#         # 数满足条件的A有几个
#         sum_ = sum(A[0])
#         if (sum(A[0])==sum(A[1])==sum(A[2])
#         ==sum([A[0][0],A[1][0],A[2][0])==sum([A[0][1],A[1][1],A[2][1])==sum([A[0][2],A[1][2],A[2][2])
#         ==sum([A[0][0],A[1][1],A[2][2])==sum([A[0][2],A[1][1],A[2][0])):
#             for j in range(3):


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(array):
            s = array[0][0]+array[0][1]+array[0][2]
            if len(set(array[0]))==1 and len(set(array[1]))==1 and len(set(array[2]))==1:
                return False
            for a in array:
                for b in a:
                    if b<1 or b>9:
                        return False
            for i in range(3):
                if array[i][0]+array[i][1]+array[i][2]!=s:
                    return False
            for j in range(3):
                if array[0][j]+array[1][j]+array[2][j]!=s:
                    return False
            if array[0][0]+array[1][1]+array[2][2]!=s or array[2][0]+array[1][1]+array[0][2]!=s:
                return False
            return True
                    
        num = 0
        if len(grid)<3 or len(grid[0])<3:
            return 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                array = []
                raw = grid[i:i+3]
                for r in raw:
                    array.append(r[j:j+3])
                if magic(array):
                    num += 1
        return num