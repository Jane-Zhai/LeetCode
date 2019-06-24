class Solution:
    def convertToTitle(self, n: int) -> str:
        """
        给定一个正整数，返回它在 Excel 表中相对应的列名称。
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB 
        ...
        """
        res = str()
        while n:
            n -= 1
            res += chr(n % 26 + ord('A'))
            n = n // 26
        return res[::-1]


sol = Solution()
print(sol.convertToTitle(28))