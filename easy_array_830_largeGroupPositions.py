class Solution:
    def largeGroupPositions(self, S):
        """
        我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置
        最终结果按照字典顺序输出。
        """



class Solution2:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        res = []

        for i in range(0, len(S)):
            # print(S[j], j, S[i], i)
            if S[i] != S[j]:
                if i - j >= 3:
                    res.append([j, i-1])
                j = i

        if i == len(S) - 1 and i - j >= 2:
            res.append([j, i])

        return res


class Solution3:
    def largeGroupPositions(self, S):
        i,result=0,[]
        while i<len(S):
            j=i+1
            while j<len(S) and S[j]==S[i]:
                j+=1
            if j-i>2:
                result.append([i,j-1])
            i=j
        return result


sol = Solution2()
print(sol.largeGroupPositions("abcdddeeeeaabbbcd"))