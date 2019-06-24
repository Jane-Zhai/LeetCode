class Solution:
    def validMountainArray(self, A):
        """
        给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
        """
        top = max(A)
        topIndex = A.index(top)
        if len(A)-1==topIndex or topIndex == 0:
            return False
        for i in range(1,topIndex+1):
            while A[i]<=A[i-1]:
                return False
        for i in range(topIndex+1,len(A)):
            while A[i]>=A[i-1]:
                return False

        return True


sol = Solution()
print(sol.validMountainArray([5,4,3]))