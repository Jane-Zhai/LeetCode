class Solution:
    def generate(self, numRows):
        """
        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle
        给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        """
        tri = dict()
        tri[1] = [1]
        for i in range(2,numRows+1):
            tri[i] = [1,]           
            for k in range(1,i-1):
                tri[i].append(tri[i-1][k-1]+tri[i-1][k])
            tri[i].append(1)
        ret = [tri[1],]
        for j in range(2,numRows):
            ret.append(tri[j])
        return ret


class Solution2:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            now = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n-1]+pre[n]
            result += [now]
            pre = now
        return result


class Solution3(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1,numRows):
            res.append(map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1]))
        return res


sol = Solution3()
print(sol.generate(5))