class Solution:
    def addToArrayForm(self, A, K):
        """
        对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
        给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
        """
        X = 0
        for a in A:
            X = X*10+a
        add = X + K
        ret = list()

        while add>0:
            a = add % 10
            ret.insert(0,a)
            add = add//10
        return ret


class Solution2:
    def addToArrayForm(self, A, K):
        Astr = ''.join([str(i) for i in A])
        M = int(Astr)
        C = str(M+K)
        P = [c for c in C]
        ans = [int(p) for p in P]
        return ans


sol = Solution2()
print(sol.addToArrayForm([9,9,9,9],1))