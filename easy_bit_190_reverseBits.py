class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 颠倒给定的 32 位无符号整数的二进制位。

        # 利用十进制转二进制的方法，考虑十进制13
        # 13 ／ 2 = 6 ----1
        # 6 ／2 = 3 ----0
        # 3 ／2 = 1 ----1
        # 1 ／2 = 0 ----1
        # 二进制是1101，前面补全0，而反转的二进制是1011，后面补全0
        # 所以我们只需要按照除的顺序依次进入数组，后面不组32位用0补齐即可。

        stack = list()
        while n:
            stack.append(n%2)
            n //= 2
        while len(stack) < 32:
            stack.append(0)
        ret = 0
        for num in stack:
            ret = ret*2 + num

        return ret



class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 二进制的本质
        ans = 0
        i = 32
        while i:
            ans <<= 1
            ans += n & 1
            n >>= 1
            i -= 1

        return ans


class Solution3:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 转化成二进制
        # 不一定够32位，把不够的补上
        # 翻转
        # 转化成十进制
        bit = bin(n)
        length = len(bit[2::])
        full_bit = (32 - length) * '0' + bit[2::]
        reverse_string = '0b' + full_bit[::-1]
        num = int(reverse_string, 2)
        return num


sol = Solution2()
print(sol.reverseBits(1))