class Solution:
    def isMonotonic(self, A):
        """
        判断是否是单调数列
        """
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                for j in range(i,len(A)):
                    while A[j] < A[j-1]:
                        return False
            elif A[i] < A[i-1]:
                for j in range(2,len(A)):
                    while A[j] > A[j-1]:
                        return False
            else:
                continue
        return True


sol = Solution()
print(sol.isMonotonic([4,2,3]))   