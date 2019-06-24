class Solution:
    def pivotIndex(self, nums):
        """
        中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
        如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
        """
        # index = len(nums)//2

        # while index < len(nums)-1 and index > 0:
        #     left = sum(nums[:index])
        #     right = sum(nums[(index+1):(len(nums))])

        #     if left == right:
        #         return index
        #     elif left < right:
        #         index += 1               
        #     else:
        #         index -= 1

        # return -1

        index = len(nums)//2

        left = sum(nums[:index])
        right = sum(nums[(index+1):(len(nums))])

        while index < len(nums)-1 and index > 0:
            if left == right:
                return index
            elif left < right:
                left += nums[index]
                right -+ nums[index+1]
                index += 1               
            else:
                left -= nums[index-1]
                right += nums[index]
                index -= 1

        return -1

sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
