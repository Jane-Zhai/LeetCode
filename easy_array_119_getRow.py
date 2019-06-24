class Solution:
    def getRow(self, rowIndex):
        """
        Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
        Note that the row index starts from 0
        给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
        """
        
        for i in range(rowIndex+1):
            new = [1]*(i+1)
            if i>1:              
                for k in range(1,i):
                    new[k]=pre[k-1]+pre[k]
            pre=new
        return new


class Solution2(object):
    def getRow(self, rowIndex):
        """
        Could you optimize your algorithm to use only O(k) extra space?
        二项式定理
        """
        if rowIndex==0:
            return [1]
        list1=[]
        i=j=1
        h=rowIndex
        while i<rowIndex:
            list1.append(h//j)
            h*=rowIndex-i
            j*=i+1
            i+=1
        list1.append(1)
        list1.insert(0,1)
        return list1


class Solution3(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex + 1):
            res = list(map(lambda x, y: x + y, res + [0], [0] + res))
        return res


sol = Solution3()
print(sol.getRow(3))
