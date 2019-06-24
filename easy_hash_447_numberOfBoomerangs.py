class Solution:
    def numberOfBoomerangs(self, points):
        """
        给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
        找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
        """
        res=0
        
        for i in range(len(points)):
            d = dict()
            for j in range(len(points)):
                dd=(points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                d[dd]=d.get(dd,0)+1
            for dd in d:
                res += (d[dd]) * (d[dd]-1)
        return res


sol = Solution()
print(sol.numberOfBoomerangs([[-10,0],[0,0],[10,0],[20,0]]))