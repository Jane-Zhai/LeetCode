class Solution:
    def findMaxAverage(self, nums, k):
        """
        给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
        """
        sum_=0
        for i in range(len(nums)-k+1):
            add_ = 0
            for j in range(i,i+k):
                add_ += nums[j]
                sum_ = max(sum_, add_)
        return sum_/k


class Solution2(object):
    def findMaxAverage(self, nums, k):
        maxi=sum(nums[:k])
        temp=maxi
        for i in range(len(nums)-k):
            temp=temp-nums[i]+nums[i+k] 
            # 不要不断用 sum 进行计算sum(nums[i:i+k]),这样耗时
            maxi=max(maxi,temp)
        return maxi/float(k)


sol = Solution()
print(sol.findMaxAverage([1,2,3,4,5,6,7,8],4))