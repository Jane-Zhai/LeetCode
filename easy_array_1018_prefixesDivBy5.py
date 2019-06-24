class Solution:
    def prefixesDivBy5(self, A):
        """"
        给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
        返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false
        """
        a = 0
        ans = list()
        for i in A:
            a = a*2 + i
            if a%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

            
sol = Solution()
print(sol.prefixesDivBy5([1,1,1,0,1]))