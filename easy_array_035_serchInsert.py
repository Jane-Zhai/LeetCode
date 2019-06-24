class Solution1(object):
    def searchInsert(self, nums, target):
        """
        Given a sorted array and a target value, return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.

        You may assume no duplicates in the array.

        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
        如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

        你可以假设数组中无重复元素。
        """

        if nums[-1]<target:
            nums.append(target)
            return nums,nums.index(target)
        else:
            for i, num in enumerate(nums):
                if num == target:
                    return nums,i
                elif num > target:
                    # nums.append(target)
                    # nums.sort()
                    # return nums.index(target)  
                    nums.insert(i, target)   
                    return nums,i       
            

class Solution2(object):
    def searchInsert(self, nums, target):
        """
        二分法
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right - left) / 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


sol = Solution2()
nums = [1,2,4,5]
print(sol.searchInsert(nums, 6))
