class Solution:
    def moveZeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        Do not return anything, modify nums in-place instead.
        """
        for i,num in enumerate(nums):
            if num == 0:
                nums.pop(i)
                nums.append(0)
        return nums


class Solution2:
    def moveZeroes(self, nums):
        for i,num in enumerate(nums):
            if num == 0:
                for k in range(i,len(nums)-1):
                    nums[k] = nums[k+1]
            nums[len(nums)-1] = 0
        return nums


class Solution3(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index,len(nums)):
            nums[i] = 0


sol = Solution3()
print(sol.moveZeroes([0,1,0,3,12]))