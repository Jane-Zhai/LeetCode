class Solution(object):
    def isPowerOfFour(self, num):
        """
        给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
        :type num: int
        :rtype: bool
        """
        # 4的倍数首先要满足2的倍数的条件，然后他减1要是3的倍数。
        return num>0 and not (num & (num-1)) and (num-1)%3==0


class Solution2(object):
    def isPowerOfFour(self, num):
        # 4的倍数首先要满足2的倍数的条件，然后他减1要是3的倍数。
        return not (num & (num-1)) and (num & 0x55555555!=0)

sol = Solution2()
print(sol.isPowerOfFour(16))