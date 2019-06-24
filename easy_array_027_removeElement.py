class Solution1(object):
    def removeElement(self, nums, val):
        """
        Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

        给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
        不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素
        """
        
        for num in nums[::-1]:
            if num == val:
                nums.remove(num)
        # return len(nums)
        return nums,len(nums)


class Solution2(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index = index + 1
        return index
        

result = Solution1()
print(result.removeElement([1,1,2,1,3,4,3,1,1,1,1,1],1))