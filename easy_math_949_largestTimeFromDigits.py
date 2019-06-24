class Solution:
    def largestTimeFromDigits(self, A) -> str:
        """
        给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
        最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
        以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
        """
        if 2 in A:
            res = "2"
            A.remove(2)
            for i in list(range(4))[-1::-1]:
                if i in A:
                    res += str(i)
                    A.remove(i)
                    res += ":"
                    break
            if len(res) != 3:
                res = "0"
                A.append(2)
        elif 1 in A:
            res = "1"
            A.remove(1)
        elif 0 in A:
            res = "0"
            A.remove(0)
        else:
            return ""
        
        if len(res)==1:
            for i in list(range(10))[-1::-1]:
                if i in A:
                    res += str(i)
                    res += ":"
                    A.remove(i)
                    break

        for i in list(range(6))[-1::-1]:
            if i in A:
                res += str(i)
                A.remove(i)
                break
        
        res += str(A[0])
        return res
        
import itertools
class Solution2:
    def largestTimeFromDigits(self, A) -> str:
        maxm = 0
        time = []
        T = ''
        for i in itertools.permutations(A):
            i = list(i)
            if i[0] > 2:
                continue
            if i[0] == 2 and i[1] > 3:
                continue
            if i[2] > 5:
                continue
            if (i[0]*10+i[1])*60+i[2]*10+i[3] >= maxm:
                maxm = (i[0]*10+i[1])*60+i[2]*10+i[3]
                time = i
        if time:
            time.insert(2,':')
        else:
            return ""
        for t in time:
            T += str(t)
        return T


sol = Solution()
print(sol.largestTimeFromDigits([0,0,1,0]))
