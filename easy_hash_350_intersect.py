class Solution:
    def intersect(self, nums1, nums2):
        """
        给定两个数组，编写一个函数来计算它们的交集。
        """
        inter = set(nums1) & set(nums2)
        l = list()
        for i in inter:
            l += [i] * min(nums1.count(i),nums2.count(i))
        return l


sol = Solution()
print(sol.intersect([1,2,2,1],[2,2]))