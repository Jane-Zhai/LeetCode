class Solution():
    def missingNumber(self, nums):
        """
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
        给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
        """
        for i,num in enumerate(nums):
            if i not in nums:
                return i


class Solution2:
    """
    求和，然后和1到n项的数列和对比，相差的数就是缺的这个数
    """
    def missingNumber(self, nums) -> int:
        t=len(nums)
        return sum(range(t+1))-sum(nums)  # 数列求和
        # return n * (n+1) / 2 - sum(nums)  # 等差数列求和


class Solution3:
    """
    求和，然后和1到n项的数列和对比，相差的数就是缺的这个数
    """
    def missingNumber(self, nums) -> int:
        res = len(nums)
        for i,val in enumerate(nums):
            res ^= i
            res ^= val
        return res


sol = Solution3()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))