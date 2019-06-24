class Solution:
    def largestTriangleArea(self, points) -> float:
        """
        给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
        """
        # 利用公式abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
        area = 0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    x3 = points[k][0]
                    y3 = points[k][1]
                    area = max(area,abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)))
        
        return area/2


sol = Solution()
print(sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))