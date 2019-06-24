class Solution(object):
    def letterCasePermutation(self, S):
        """
        给定一个字符串S，通过将字符串S中的每个字母转变大小写，
        我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for c in S:
            res = [i+c for i in res]+[i+c.swapcase() fonr i in res if c.isalpha()]
        return res


sol = Solution()
print(sol.letterCasePermutation("a1b2")) 



# 总结一下，简单题中涉及的二进制的基本知识点有：
# 1、两个相同的数，按位异或值为0
# 2、一个数与比他小1的数按位与运算，相当于把该数的二进制位中的最后一位1变为0
# 3、二进制的加法，可以用异或和按位与运算来解决，参照371题。