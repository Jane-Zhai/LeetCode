class Solution:
    def thirdMax(self, nums):
        """
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
        给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
        """
        retnum = 1
        nums.sort(reverse=True)  # 复杂度错
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                retnum += 1
                if retnum == 3:
                    return nums[i]
        return nums[0]


class Solution2(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2= max3=None
        for num in nums:
            if num > max1:
                max2,max3 = max1,max2
                max1=num
            elif num > max2 and num < max1:
                max2,max3= num,max2
            elif num > max3 and num < max2:
                max3 = num
        return max1 if max3==None else max3


sol = Solution2()
print(sol.thirdMax([1,2,4,5,3,6,5]))
