class Solution:
    def minMoves(self, nums) -> int:
        """
        给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。
        每次移动可以使 n - 1 个元素增加 1。
        """
        # n-1个数同时加一，就好比每次有一个数自身减一，因为只能做减法，所以数组最后的数只能是最小值。
        # 这样的话每个元素减去最小值求其和就是答案。
        sum_ = 0
        minmun = min(nums)
        for i in nums:
            sum_ += i - minmun
        return sum_


class Solution2(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)


sol = Solution()
print(sol.minMoves([1,2,3,4]))