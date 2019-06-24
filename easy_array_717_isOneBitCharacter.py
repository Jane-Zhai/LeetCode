class Solution:
    def isOneBitCharacter(self, bits):
        """
        有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
        现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
        """
        if bits[len(bits)-1] != 0:
            return False
        
# 从前看，第一个不为0 的数，
# 出现1， 需要隔一个数看， 如果是0 ，直到不为0 ，
#                         如果是1，
        i = 0
        while i < len(bits):
            while bits[i] != 0:
                i += 2
                if i == len(bits)-2:
                    return False
                break
            i += 1
        return True


sol = Solution()
print(sol.isOneBitCharacter([1, 1, 1, 0]))


def isOneBitCharacter(self, bits):
    """只与最后一个元素0的前面的连续1的个数有关系。"""
        num=len(bits)-1
        count=0
        if bits[-1] == 1:
            return False
        for i in range(num-1,-1,-1):   #倒序遍历
            if bits[i] == 1:
                count=count+1
            else:
                break
        if (count % 2)== 0:
            return True
        else:
            return False