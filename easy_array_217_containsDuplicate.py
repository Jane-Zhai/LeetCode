class Solution:
    def containsDuplicate(self, nums):
        """
        Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct
        给定一个整数数组，判断是否存在重复元素。
        如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
        """
        for num in nums:
            if nums.count(num)>1:
                return True
        return False


class Solution2():
    def containsDuplicate(self, nums):
        for i in range(1,len(nums)-1):
            for j in range(0,len(nums)-2):
                if nums[i] == nums[j]:
                    return True
        return False


class Solution3:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


sol = Solution2()
print(sol.containsDuplicate([1,2,3]))