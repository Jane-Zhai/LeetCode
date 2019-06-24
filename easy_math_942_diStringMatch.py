class Solution:
    def diStringMatch(self, S: str):
        """
        给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
        返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
            如果 S[i] == "I"，那么 A[i] < A[i+1]
            如果 S[i] == "D"，那么 A[i] > A[i+1]
        """
        l = list(range(len(S)+1))
        res = list()
        for i in S:
            if i == 'I':
                res.append(l[0])
                l=l[1:]
            else:
                res.append(l[-1])
                l.pop()
        res.append(l[0])
        return res

class Solution2:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        A = []
        for i in S:
            if i == 'I':
                A.append(left)
                left += 1
            else:
                A.append(right)
                right -= 1
        A.append(right)
        return A


sol = Solution()
print(sol.diStringMatch("DDI"))
