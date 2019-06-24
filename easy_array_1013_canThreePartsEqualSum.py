class Solution:
    def canThreePartsEqualSum(self, A):
        """
        给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
        形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
        """
        add = 0
        if sum(A)%3 != 0:
            return False
        else:
            ave = sum(A)/3
            for a in A:
                add += a
                while add == ave:
                    add = 0
                    break
            if add == 0:
                return True
            else:
                return False
                    

class Solution2:
    def canThreePartsEqualSum(self, A):
        """
        首选算A的累加和能否被3整除，不可以那分不了3等分。
        双指针前后向中间逼近，不用考虑中间那段怎么分，只要左右两段累加和等于3等分的数值，中间剩的那段也就找到了。
        """
        ans = sum(A)
        if ans % 3 != 0:
            return False
        
        avg = int(ans / 3)
        
        
        i = 0
        j = len(A) - 1
        res = False
        lans,rans = 0,0
        while i < j:
            if lans != avg:
                lans += A[i]
                i += 1
            
            if rans != avg:
                rans += A[j]
                j -= 1
            
            if lans == avg and rans == avg:
                res = True
                break
        
        return res


sol = Solution()
print(sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))