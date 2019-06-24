class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """
        每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。注意，除 N = 0 外，任何二进制表示中都不含前导零。
        二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。
        给定十进制数 N，返回其二进制表示的反码所对应的十进制整数。
        """
        # a = len(bin(N)[2:])*'1'
        # b = int(a,2)
        # c = b ^ N

        return (int(len(bin(N)[2:])*'1',2)^N)


sol = Solution()
print(sol.bitwiseComplement(5))

# if N == 0:
#     return 1
# i = 1
# while i <= N:
#     i *= 2
# return i-N-1


# 输入N与取反得到的输出的和是一个固定值，这个值2的l次方减一（l为N的二进制长度）
# return 2**(len(bin(N))-2)-1-N