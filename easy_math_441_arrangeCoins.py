class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
        给定一个数字 n，找出可形成完整阶梯行的总行数。
        n 是一个非负整数，并且在32位有符号整型的范围内。
        """
        coin = 1
        i = 1
        while coin <= n:
            i += 1
            coin += i
        return i-1


sol = Solution()
print(sol.arrangeCoins(0))
            