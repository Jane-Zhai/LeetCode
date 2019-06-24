class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。
        （注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）
        :type L: int
        :type R: int
        :rtype: int
        L, R 是 L <= R 且在 [1, 10^6] 中的整数。
        R - L 的最大值为 10000。
        """
        # 10的6次方 对应2的20次方 所以不用统计太多质数
        num = 0
        for i in range(L,R+1):
            c = self.count1(i)
            if c in [2,3,5,7,11,13,17,19]:
                num += 1

        return num
                
    
    def count1(self, num):
        c = 0
        while num:
            num = num & (num-1)
            c += 1
        return c


class Solution2(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int 
        """
        res = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(L, R+1):
            if bin(i).count('1') in prime:
                res += 1
        return res


sol = Solution()
print(sol.countPrimeSetBits(10,15)) 