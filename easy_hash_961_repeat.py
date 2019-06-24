class Solution:
    def repeatedNTimes(self, A):
        """
        在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
        返回重复了 N 次的那个元素。
        """
        A.sort()
        if (A[0] == A[1]):
            return A[0]
        return A[len(A)//2]


class Solution2:
    def repeatedNTimes(self, A):
        A=sorted(A)
        mid=len(A)//2
        return A[mid] if A[mid]==A[mid+1] else A[mid-1]


class Solution3:
    def repeatedNTimes(self, A: List[int]) -> int:
        for a in A:
            if(A.count(a) > 1):
                return a


sol = Solution()
print(sol.repeatedNTimes([4,2,1,2,5,2,3,2])) 