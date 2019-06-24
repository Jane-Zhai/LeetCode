class Solution1(object):
    def maxSubArray(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        """
        add = []
        for i,num in enumerate(nums):
            add.append(num)
            summation = num
            for k in range(i+1, len(nums)):               
                summation += nums[k]
                add.append(summation)
        return max(add)


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum


class Solution3(object):
    def maxSubArray(self, nums):
        ret = nums[0]
        summation = 0
        for num in nums:
            if summation>0:
                summation += num
            else:
                summation = num
            ret = max(summation, ret)
        return ret


class Solution4(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return nums,max(nums)


sol = Solution2()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))