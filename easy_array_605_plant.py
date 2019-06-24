class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed[0] == 0 and flowerbed[1]==0:
            flowerbed[0]=1
            n -= 1
            while n <= 0:
                    return True
        for i in range(1,len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                while n <= 0:
                    return True
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            n-=1
            while n <= 0:
                    return True

        return False


class Solution2:
    def canPlaceFlowers(self, flowerbed, n):
        """左右各加个0"""
        flowerbed.insert(1,0)
        flowerbed.append(0)
        for i in range(1,len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                while n <= 0:
                    return True

        return False

sol = Solution2()
print(sol.canPlaceFlowers([0,0,0,1,0,0,0],2))
        