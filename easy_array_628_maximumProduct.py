class Solution:
    def maximumProduct(self, nums):
        """
        给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
        给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
        输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
        """
        nums.sort()            
        if nums[-1]*nums[-2] < nums[0]*nums[1]:
            return nums[0]*nums[1]*nums[-1]
        else:
            return nums[-1]*nums[-2]*nums[-3]

sol = Solution()
print(sol.maximumProduct([-1,-2,0,1,2,3]))