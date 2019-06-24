class Solution:
    def isHappy(self, n):
        """
        一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
        """

        """
        用列表保存出现过的数，当出现重复的数字的时候，说明出现了循环，循环有两种情况，一种不是hayyp数，循环的数必不是1，如果是happy数，那么会出现1的不断循环
        """
        c = set()
        while not n in c:
            c.add(n)
            n = sum([int(x)**2 for x in str(n)])
        return n == 1


class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        使用追赶法，快的指针每次前进两步，慢的指针每次只前进一步，当快的指针追上慢的指针即二者数字相同时，同样说明出现了循环，情况同上
        """
        slow = n
        quick = sum([int(x) ** 2 for x in str(n)])
        while quick != slow:
            quick = sum([int(x) ** 2 for x in str(quick)])
            quick = sum([int(x) ** 2 for x in str(quick)])
            slow = sum([int(x) ** 2 for x in str(slow)])
        return slow == 1


sol = Solution()
print(sol.isHappy(19))