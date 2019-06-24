class Solution:
    def dominantIndex(self, nums):
        """
        在一个给定的数组nums中，总是存在一个最大元素 。
        查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
        如果是，则返回最大元素的索引，否则返回-1。
        """
        num = max(nums)
        index = nums.index(num)
        for i in range(len(nums)):
            if num < 2*nums[i] and i != index:
                return -1
        return index


sol = Solution()
print(sol.dominantIndex([1, 2, 3, 4]))
