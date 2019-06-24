class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
        给出两个整数 x 和 y，计算它们之间的汉明距离。
        """
        z = x ^ y
        count = 0
        while z:
            z = z & (z-1)
            count += 1
        return count


sol = Solution()
print(sol.hammingDistance(1,4)) 
        