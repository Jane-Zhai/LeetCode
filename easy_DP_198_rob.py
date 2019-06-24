class Solution(object):
    def rob(self, nums):
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
        影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
        
        给定一个代表每个房屋存放金额的非负整数数组，
        计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

        :type nums: List[int]
        :rtype: int
        """
        return max(sum(nums[0::2]),sum(nums[1::2]))


class Solution2():
    def rob(self, nums):
        l = len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        index = list()
        index.append(nums[0])
        index.append(max(index[0],nums[1]))
        for i in range(2,l):
            index.append(max(index[i-1], index[i-2]+nums[i]))
        return index[l-1]

sol = Solution2()
print(sol.rob([2,7,9,3,1])) 