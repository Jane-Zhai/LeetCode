class Solution:
    def flipAndInvertImage(self, A):
        """
        给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
        """
        fliprow = list()

        for row in A:
            fliprow.append(row[::-1])
        
        for row in fliprow:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1

        return fliprow



sol = Solution()
print(sol.flipAndInvertImage( [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
