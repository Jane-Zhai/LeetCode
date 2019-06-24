class Solution:
    def findShortestSubArray(self, nums):
        """
        给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
        你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
        
        使用字典的数据结构来统计信息，其中 freqDict[nums[i]] = [freq, s, e] 表示数字 nums[i] 出现的次数为 freq ，
        第一次出现的位置为 s ，最后一次出现的位置为 e 。
        """
        dic = dict()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [1,i,i]
            else:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i

        n=0
        for i in dic.values():
            if n < i[0]:
                n,ilen = i[0], i[2]-i[1]+1
            elif n == i[0]:
                ilen = min(ilen, i[2]-i[1]+1)
                
        return ilen


sol = Solution()
print(sol.findShortestSubArray([5,3,3,5,3,5]))
print(sol.findShortestSubArray([3,5,5,3,5,3]))