class Solution:
    def arrayPairSum(self, nums):
        """
        Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
        给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大
        """

        
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        就是返回排序后第1，3，5，。。2n-1小的数
        """
        return sum(sorted(nums)[::2])


sol = Solution2()
print(sol.arrayPairSum([1,4,3,2]))