class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
        """
        
        if (c==0):
            return True
        
        while(c%4==0):
            c//=4
        if (c%4==3):
            return False        # ???? 奇偶分类讨论易知
        
        
        small=0
        big=int(c**0.5)
        while (small<=big):
            temp=small**2+big**2
            if (temp==c):
                return True
            elif (temp<c):
                small+=1
            else:
                big-=1
        
        return False