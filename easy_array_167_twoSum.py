class Solution:
    def twoSum(self, numbers, target):
        """
        Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
        The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
        Note:
        Your returned answers (both index1 and index2) are not zero-based.
        You may assume that each input would have exactly one solution and you may not use the same element twice.
        
        给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
        函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
        说明:
        返回的下标值（index1 和 index2）不是从零开始的。
        你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
        """
        for i,num in enumerate(numbers):
            if num <= target:
                sub = target-num
                if sub in numbers:
                    return i+1, numbers.index(sub)+1


sol = Solution()
print(sol.twoSum([2, 7, 11, 15],111))