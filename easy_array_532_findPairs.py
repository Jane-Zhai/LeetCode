class Solution:
    def findPairs(self, nums, k):
        """
        Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
        给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.
        """

import collections
class Solution2(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        如果k大于0，则返回两个set的交集
        如果k=0，则计数，找出出现1次以上的元素的个数
        如果k小于0，返回0
        """
        if k>0:
            return len(set(nums) & set(n+k for n in nums))
        elif k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
            
        else:
            return 0


sol = Solution2()
print(sol.findPairs([3, 1, 4, 1, 5],0)) 