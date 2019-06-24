class Solution:
    def titleToNumber(self, s: str) -> int:
        """
        给定一个Excel表格中的列名称，返回其相应的列序号。
            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28 
            ...
        """
        n=0
        c = (len(s)-1) * 26
        for i in s:
            n += c * (ord(i)-ord('A') + 1)
            c//=26
        return n


sol = Solution()
print(sol.titleToNumber('ZY'))