class Solution:
    def findLengthOfLCIS(self, nums):
        """给定一个未经排序的整数数组，找到最长且连续的的递增序列。
        """
        count_ = 1
        maxlen = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count_ += 1
                maxlen = max(maxlen, count_)
            else:              
                count_ = 1
        return maxlen


sol = Solution()
print(sol.findLengthOfLCIS([5,2,3,4,3]))