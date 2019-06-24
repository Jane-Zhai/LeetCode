class Solution:
    def islandPerimeter(self, grid):
        """
        给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
        网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
        岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
        """
        l = len(grid[0])
        grid = [[0]*l]+grid+[[0]*l]
        grid = [[0]+i+[0] for i in grid]
        count = 0

        for i in range(1,len(grid)-1):
            for bit in range(1,l):
                if grid[i][bit] == 1:
                    if grid[i-1][bit]==0:
                        count += 1
                    if grid[i][bit-1]==0:
                        count += 1
                    if grid[i+1][bit]==0:
                        count += 1
                    if grid[i][bit+1]==0:
                        count += 1

        return count

class Solution2(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        数学推理：周长=个数*4-重合边*2； 计算个数和重合边
        在统计邻居的时候，为了避免重复，循环每一个元素时只统计其上方和左方元素是否为1
        """
        num = 0
        neighbor = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = num + 1
                    if i > 0 and grid[i-1][j] == 1:
                        neighbor += 1
                    if j>0 and grid[i][j-1] == 1:
                        neighbor += 1
        return num * 4 - neighbor *2


sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))