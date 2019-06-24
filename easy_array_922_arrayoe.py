class Solution:
    def sortArrayByParityII(self, A):  
        """
        给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
        对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
        你可以返回任何满足上述条件的数组作为答案。
        """
        index = 0
        for x in range(len(A)):
            index = x
            if x % 2 == 0:
                while A[x] % 2 != 0:
                    A[x],A[index + 1] = A[index + 1],A[x]
                    index+=1
            else:
                while A[x] % 2 != 1:
                    A[x],A[index + 1] = A[index + 1],A[x]
                    index+=1
        return A


sol = Solution()
print(sol.sortArrayByParityII([4,2,2,5,7,9]))  
