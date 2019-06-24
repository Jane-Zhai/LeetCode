class Solution:
    def checkPossibility(self, nums):
        """"
        给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
        """
        count_ = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count_ += 1
                while count_>1:
                    return False
        return True


sol = Solution()
print(sol.checkPossibility([3,1,2,3,8]))