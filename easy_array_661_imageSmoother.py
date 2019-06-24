class Solution:
    def imageSmoother(self, M):
        """
        包含整数的二维矩阵 M 表示一个图片的灰度。
        你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，
        平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
        """


class Solution2(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        深度学习
        """
        #padding 外边加一圈
        m = len(M[0])
        N = [[0.5]+i+[0.5] for i in M]
        N = [[0.5]*(m+2)] + N + [[0.5]*(m+2)]
        
        #卷积
        for i in range(1,len(N)-1):
            for j in range(1,len(N[0])-1):
                total = [N[i-1][j-1],N[i][j-1],N[i+1][j-1],N[i-1][j],N[i][j],N[i+1][j],N[i-1][j+1],N[i][j+1],N[i+1][j+1]]
                sums,k = 0,0
                for _ in total:
                    if _ != 0.5:
                        sums += _
                    else:
                        k += 1
                M[i-1][j-1] = int(sums/(9-k))
        return M



sol = Solution2()
print(sol.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))