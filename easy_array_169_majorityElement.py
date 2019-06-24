class Solution:
    def majorityElement(self, nums):
        """
        Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
        You may assume that the array is non-empty and the majority element always exist in the array.
        给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
        你可以假设数组是非空的，并且给定的数组总是存在众数。
        """
        for num in nums:
            if nums.count(num) > (len(nums)//2):
                return num


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
        """
        cand = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                cand, count = i, 1
            else:
                if i == cand:
                    count = count + 1
                else:
                    count = count - 1
        return cand

sol = Solution2()
print(sol.majorityElement([4,3,4,2,4,3,4]))