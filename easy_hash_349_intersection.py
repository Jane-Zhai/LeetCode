class Solution:
    def intersection(self, nums1, nums2):
        """
        给定两个数组，编写一个函数来计算它们的交集。
        """
        lis = list()
        n1 = set(nums1)
        n2 = set(nums2)
        for num in n1:
            if num in n2:
                lis.append(num)
        return lis


class Solution2:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

sol = Solution2()
print(sol.intersection([1,2,2,1],[2,2]))