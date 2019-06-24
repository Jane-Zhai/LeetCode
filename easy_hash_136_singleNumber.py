class Solution:
    def singleNumber(self, nums):
        """
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        你的算法应该具有线性时间复杂度。

        这道题虽然放在了hashtable里，但其实用二进制的算法更容易求解
        两个相同数的二进制异或为0，所以遍历一边数组，出现两次的异或值变为0，那么剩下的数就是出现一次的数
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))