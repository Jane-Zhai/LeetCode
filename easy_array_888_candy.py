class Solution:
    def fairCandySwap(self, A, B):
        """
        交换糖果使二人一样
        """
        acandy = sum(A)
        bcandy = sum(B)
        average = (acandy + bcandy) / 2
        if acandy < bcandy:
            for a in A:
                b = average - acandy + a
                if b in B:
                    return [int(a),int(b)]
        else:
            for b in B:
                a = average - bcandy + b
                if a in A:
                    return [int(a),int(b)]

                
sol = Solution()
print(sol.fairCandySwap([1,5,2], [2,4]))