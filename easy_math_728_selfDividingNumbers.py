class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        """
        自除数 是指可以被它包含的每一位数除尽的数。
        例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
        还有，自除数不允许包含 0 。
        给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
        """
        res = list()
        for i in range(left,right+1):
            if i < 10:
                res.append(i)
            else:
                # 判断是几位数
                count = 1
                while i//(10**count)>0:
                    count += 1
                # 判断能否除尽
                s = str(i)
                for j in s:
                    if j!='0' and i%int(j)==0:
                        count -= 1
                if count == 0:
                    res.append(i)
        return res
             
class Solution2(object):
    def selfDividingNumbers(self, left, right):
        def self_div(num):
            if '0' in str(num):
                return False
            res = True
            for s in str(num):
                if num % int(s) != 0:
                    res = False
            return res
        return [i for i in range(left, right + 1) if self_div(i)]


sol = Solution2()
print(sol.selfDividingNumbers(1,22))