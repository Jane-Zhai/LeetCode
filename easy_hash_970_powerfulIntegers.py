class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
        返回值小于或等于 bound 的所有强整数组成的列表。
        你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
        """
        i = 0
        j = 0
        res = list()

        while True:
            while True:
                b = x**i+y**j
                if b<=bound:
                    res.append(b)
                else:
                    break
                j += 1
            i += 1
            if x**i>bound:
                break
            j = 0

        return list(set(res))


class Solution2:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # 考虑x,y均为1的情况
        if x +y == 2:
            if x +y <= bound:
                return [x+y]
            else:
                return []
            
        # 总是让 x 不小于 y，方便后面的判断
        if x < y:
            x,y=y,x
            
        res = set()
        
        # 考虑 y 为1的特殊情况
        if y == 1:
            cur = 1
            while cur+y <=bound:
                res.add(cur+y)
                cur *=x
            return list(res)
        # x,y 均不为1，则指数分别都从0开始进行迭代
        # 保留每次的结果，把指数运算降为乘法运算
        i=0
        cur_x = 1
        while cur_x < bound:
            cur_y=1
            while cur_x + cur_y <=bound:
                res.add(cur_x+cur_y)
                cur_y *=y
            cur_x *=x
        return list(res)


sol = Solution()
print(sol.powerfulIntegers(2,3,10)) 
