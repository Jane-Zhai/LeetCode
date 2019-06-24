class Solution1(object):   
    def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if (num1 == target-num2) & (i < j):
                    print([nums[i],nums[j]])


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]        
        """
        dic = dict()
        for index, value in enumerate(nums):
            sub = target-value
            if sub in dic:
                # return [dic[sub],index]
                print([dic[sub],index])
            else:
                dic[value] = index


sol = Solution2()
sol.twoSum([1,8,3,4,5], 9)
