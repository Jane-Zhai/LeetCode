class Solution:
    def commonChars(self, A):
        """
        给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
        你可以按任意顺序返回答案。
        """
        str_times = {}
        for i in A[0]:
            str_times[i] = str_times.get(i, 0) + 1
        for S in A[1:]:
            t = {}
            for i in S:
                if i in str_times:
                    t[i] = t.get(i, 0) + 1
            for i in t:
                if t[i] > str_times[i]:
                    t[i] = str_times[i]
            str_times = t
        res = []
        for i in str_times.keys():
            res += i * str_times[i]
        return res 


sol = Solution()
print(sol.commonChars(["bella","label","roller"]))