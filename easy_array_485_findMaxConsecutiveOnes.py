class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        Given a binary array, find the maximum number of consecutive 1s in this array.
        给定一个二进制数组， 计算其中最大连续1的个数。
        """
        ret = count_ = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ += 1
                ret = max(ret, count_)
            else:
                count_ = 0
        return ret


sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,1,1,0,1])) 
