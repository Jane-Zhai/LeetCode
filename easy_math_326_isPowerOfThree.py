class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        
        用到了数论的知识，3的幂次的质因子只有3，而所给出的n如果也是3的幂次，
        故而题目中所给整数范围内最大的3的幂次的因子只能是3的幂次，
        1162261467是3的19次幂，是整数范围内最大的3的幂次
        """

        return n > 0 and ((3^19)%n == 0)


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        """
        
        对于10进制数来说，10的n次幂表达为10，100，100 
        对于2进制数来说，2的n次幂的二进制表达为 10,100,100 
        3进制同理
        """
        

sol = Solution()
print(sol.isPowerOfThree(28))