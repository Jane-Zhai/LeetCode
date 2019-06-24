class Solution:
    def sortArrayByParity(self, A):
        """
        给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
        """
        for a in A[::-1]:
            if a % 2 != 0:
                A.pop(A.index(a))
                A.append(a)
        return A


class Solution2:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for j in range(len(A)):
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A


sol = Solution2()
print(sol.sortArrayByParity([2,3,4,4,1]))  