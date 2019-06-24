class Solution:
    def surfaceArea(self, grid) -> int:
        """
        在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
        每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
        返回结果形体的总表面积。
        """
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area += 4*grid[i][j]
                if grid[i][j] != 0:
                    area += 2
                    if j<len(grid[0])-1:
                        if grid[i][j+1] != 0:
                            area -= 2*min(grid[i][j],grid[i][j+1])
                    if i < len(grid)-1:
                        if grid[i+1][j] != 0:
                            area -= 2*min(grid[i][j],grid[i+1][j])
        return area


sol = Solution()
print(sol.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))


   
                