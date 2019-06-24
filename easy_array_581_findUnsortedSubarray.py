class Solution:
    def findUnsortedSubarray(self, nums):
        """
        给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
        你找到的子数组应是最短的，请输出它的长度。
        """
        a = sorted(nums)
        if a == nums:
            return 0

        for i in range (len(a)):
            if a[i] != nums[i]:
                min_ = i
                break

        a = a[::-1]
        nums = nums[::-1]
        for i in range(len(a)):
            if a[i] != nums[i]:
                max_ = i
                break

        return len(a)-max_-min_


class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_same = [a == b for (a, b) in zip(nums, sorted(nums))]
        return 0 if all(all_same) else len(nums) - all_same.index(False) - all_same[::-1].index(False)

sol = Solution()
print(sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))