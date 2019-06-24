class Solution1(object):
    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        """
        
        for num in nums[::-1]:
            if nums.count(num)>1:
                nums.remove(num)
                
        print(nums)
        print(len(nums))


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index = index + 1
                nums[index] = nums[i]

        return index + 1,nums


nums = [3,3,3,3,3,3,4,4,2,2,2,3,3,3,3,3,3]
result = Solution1()
# result.removeDuplicates(nums)
print(result.removeDuplicates(nums))