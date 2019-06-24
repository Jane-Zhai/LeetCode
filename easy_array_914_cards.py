class Solution:
    def hasGroupsSizeX(self, deck):
        """"
        给定一副牌，每张牌上都写着一个整数。
        此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
            每组都有 X 张牌。
            组内所有的牌上都写着相同的整数。
        仅当你可选的 X >= 2 时返回 true。
        """
        x=2
        for i in deck:
            x = min(x,deck.count(i))
            if x<2 or deck.count(i)%x!=0:
                return False
        return True


sol = Solution()
print(sol.hasGroupsSizeX([1,1,2,2,2,2]))
