class Solution:
    def findLHS(self, nums):
        """
        和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
        现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
        """
        res = 0
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]-nums[j] == 1 or nums[i]==nums[j]:
                    count += 1
            res = max(res,count)
        return res


import collections
class Solution2(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        使用一个字典计录元素出现的次数，随后遍历字典，找到两个差距为1的元素，这两个元素出现的次数都大于0而且相加出现的次数最大.
        """
        dic = dict(collections.Counter(nums))
        max = 0
        for i in dic:
            if dic.get(i,0) > 0 and dic.get(i+1,0) > 0 and dic.get(i,0)+dic.get(i+1,0) > max:
                max = dic.get(i,0) + dic.get(i+1,0)
        return max

sol = Solution()
print(sol.findLHS([1,3,2,2,5,2,3,7]))