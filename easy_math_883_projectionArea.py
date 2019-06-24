class Solution:
    def projectionArea(self, grid) -> int:
        """
        在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
        每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
        现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
        返回所有三个投影的总面积。
        """
        bottom = 0
        left = 0
        front = 0
        for i in range(len(grid)):
            left += max(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    bottom += 1
        n=0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                n = max(n,grid[i][j])
            front += n
        return bottom+front+left


class Solution2:
    def projectionArea(self, grid) -> int:
        if not grid:
            return 0
        
        area_xy = 0
        area_zx = 0
        area_yz = 0
        maxlist_yz = grid[0]
        
        for i in range(len(grid)):
            area_zx += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    area_xy += 1
                maxlist_yz[j] = max(maxlist_yz[j], grid[i][j])
        
        area_yz = sum(maxlist_yz)
        return area_xy + area_zx + area_yz


sol = Solution2()
print(sol.projectionArea([[1,2],[3,4]]))


                
                