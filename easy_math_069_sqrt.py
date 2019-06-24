class Solution:
    def mySqrt(self, x):
        """
        实现 int sqrt(int x) 函数。
        计算并返回 x 的平方根，其中 x 是非负整数。
        由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去
        """
        if x <= 0:
            return 0
        else:
            left = 1
            right = x
            while left<=right:
                mid = (left+right)//2
                a1 = mid*mid
                a2 = (mid-1)*(mid-1)
                if a1 >= x and a2 <= x:
                    if a1 == x:
                        return mid
                    else:
                        return mid-1
                elif a1<x and a2<x:
                    left = mid + 1
                else:
                    right = mid - 1

class Solution2:
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x/r) // 2
        return int(r)


sol = Solution()
print(sol.mySqrt(8))