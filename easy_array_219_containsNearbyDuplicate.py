class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
        给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
        """
        dic = dict()
        for i,num in enumerate(nums):
            if num in dic:
                if (i - dic[num]) <= k:
                    return True
            dic[num] = i
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))
