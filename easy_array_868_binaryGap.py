class Solution:
    def binaryGap(self, N: int) -> int:
        """
        给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。 
        如果没有两个连续的 1，返回 0 。
        """
        string = str(bin(N))[2:]
        string = str(bin(N))[2:].split('1')
        string = str(bin(N))[2:].split('1')[1:-1]
        max = -1
        for i in string:
            if len(i)>max:
                max = len(i)
        return max + 1


sol = Solution()
print(sol.binaryGap(17))